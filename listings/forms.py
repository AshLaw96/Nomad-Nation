import json
from django import forms
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import re
from .models import Caravan, Amenity, CaravanImage, Booking, Review, Reply


class CaravanForm(forms.ModelForm):
    """
    Form for creating or updating a Caravan listing.
    Includes fields for amenities, available dates, and an optional extra
    amenity.
    """
    extra_amenity = forms.CharField(
        max_length=50, required=False, help_text=_("Add extra amenities")
    )
    amenities = forms.ModelMultipleChoiceField(
        # Initially set empty
        queryset=Amenity.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    available_dates = forms.CharField(
        widget=forms.HiddenInput,
        required=False
    )

    class Meta:
        model = Caravan
        fields = [
            'title', 'description', 'berth', 'amenities', 'location',
            'price_per_night', 'available_dates'
        ]
        labels = {
            'title': _('Caravan Title'),
            'description': _('Caravan Description'),
            'berth': _('Berth Capacity'),
            'amenities': _('Select Amenities'),
            'location': _('Location'),
            'price_per_night': _('Price per Night'),
            'available_dates': _('Available Dates'),
        }
        widgets = {
            'amenities': forms.CheckboxSelectMultiple(),
            'start_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': _('Select start date')}
            ),
            'end_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': _('Select end date')}
            ),
        }

    def __init__(self, *args, **kwargs):
        """
        Custom initialization to filter the amenities based on the logged-in
        user.
        """
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['amenities'].queryset = Amenity.objects.filter(
                owner=user
            )

    def clean_extra_amenity(self):
        """
        Validates the extra amenity field to ensure it does not duplicate
        an existing amenity for the owner.
        """
        extra_amenity = self.cleaned_data.get('extra_amenity')
        if self.instance.pk is None:
            return extra_amenity
        if extra_amenity:
            if not self.instance.owner:
                raise forms.ValidationError(
                    _("Caravan must have an owner.")
                )
            if Amenity.objects.filter(
                name=extra_amenity, owner=self.instance.owner
            ).exists():
                raise forms.ValidationError(
                    _("This amenity already exists for your account.")
                )
        return extra_amenity

    def clean_available_dates(self):
        """
        Validates the available_dates field to ensure it is a properly
        formatted JSON list containing valid start and end dates.
        """
        available_dates = self.cleaned_data.get('available_dates', '[]')
        try:
            dates = json.loads(
                available_dates
            )
            if not isinstance(dates, list):
                raise forms.ValidationError(
                    _("Invalid date format. Expected a list of objects.")
                )
        except json.JSONDecodeError:
            raise forms.ValidationError(
                _("Invalid JSON format for available dates.")
            )
        # Validate each date entry
        for date_entry in dates:
            if not isinstance(date_entry, dict):
                raise forms.ValidationError(
                    _("Each date entry must be a dictionary.")
                )
            if 'start_date' not in date_entry or 'end_date' not in date_entry:
                raise forms.ValidationError(
                    _(
                        "Each date entry must contain 'start_date' and "
                        "'end_date'."
                    )
                )
            try:
                start_date = datetime.strptime(
                    date_entry['start_date'], "%Y-%m-%d"
                ).date()
                end_date = datetime.strptime(
                    date_entry['end_date'], "%Y-%m-%d"
                ).date()
            except ValueError:
                raise forms.ValidationError(
                    _("Invalid date format. Use YYYY-MM-DD.")
                )
            if start_date > end_date:
                raise forms.ValidationError(
                    _("Start date cannot be after end date.")
                )
        return dates


class CaravanImageForm(forms.ModelForm):
    """
    Form for uploading images associated with a Caravan listing.
    """
    class Meta:
        model = CaravanImage
        fields = ['image']


class BookingForm(forms.ModelForm):
    """
    Form for creating a booking request for a Caravan.
    Ensures that the selected dates are valid and do not overlap with
    existing bookings.
    """
    class Meta:
        model = Booking
        fields = [
            'name', 'email', 'phone_number', 'start_date', 'end_date',
            'message'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'phone_number': forms.TextInput(
                attrs={
                    'type': 'tel',
                    'pattern': '[0-9]+',
                    'title': 'Only numbers are allowed'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        """
        Custom initialization to associate the booking with a specific caravan.
        """
        self.caravan = kwargs.pop('caravan', None)
        super().__init__(*args, **kwargs)
        if self.caravan:
            self.instance.caravan = self.caravan

    def clean_phone_number(self):
        """
        Ensure phone_number contains only digits.
        """
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not re.fullmatch(r'\d+', phone_number):
            raise ValidationError(_("Phone number must contain only digits."))
        return phone_number

    def clean(self):
        """
        Validates that the booking has a valid caravan and that the
        requested dates do not overlap with existing accepted bookings.
        """
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        # Ensure the Booking instance has a caravan before accessing it
        if not self.instance.caravan_id:
            raise forms.ValidationError(
                _("This booking does not have an associated caravan.")
            )

        # Now safe to access
        caravan = self.instance.caravan

        if start_date and end_date:
            if start_date > end_date:
                raise forms.ValidationError(
                    _("End date must be after start date.")
                )

            # Check for overlapping bookings
            overlapping_bookings = Booking.objects.filter(
                caravan=caravan,
                status="accepted",
                start_date__lt=end_date,
                end_date__gt=start_date
            ).exclude(pk=self.instance.pk)

            if overlapping_bookings.exists():
                raise forms.ValidationError(
                    _("The caravan is not available for the selected dates.")
                )

        return cleaned_data


class ReviewForm(forms.ModelForm):
    """
    Form for submitting a review for a Caravan.
    """
    class Meta:
        model = Review
        fields = ['rating', 'comment']


class ReplyForm(forms.ModelForm):
    """
    Form for replying to a review.
    """
    class Meta:
        model = Reply
        fields = ['reply']
