import json
from django import forms
from datetime import datetime
from .models import Caravan, Amenity, CaravanImage, Booking, Review


class CaravanForm(forms.ModelForm):
    extra_amenity = forms.CharField(
        max_length=50, required=False, help_text="Add extra amenities"
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
        widgets = {
            'amenities': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['amenities'].queryset = Amenity.objects.filter(
                owner=user
            )

    def clean_extra_amenity(self):
        extra_amenity = self.cleaned_data.get('extra_amenity')
        if self.instance.pk is None:
            return extra_amenity
        if extra_amenity:
            if not self.instance.owner:
                raise forms.ValidationError(
                    "Caravan must have an owner."
                )
            if Amenity.objects.filter(
                name=extra_amenity, owner=self.instance.owner
            ).exists():
                raise forms.ValidationError(
                    "This amenity already exists for your account."
                )
        return extra_amenity

    def clean_available_dates(self):
        available_dates = self.cleaned_data.get('available_dates', '[]')
        try:
            dates = json.loads(
                available_dates
            )
            if not isinstance(dates, list):
                raise forms.ValidationError(
                    "Invalid date format. Expected a list of objects."
                )
        except json.JSONDecodeError:
            raise forms.ValidationError(
                "Invalid JSON format for available dates."
            )
        # Validate each date entry
        for date_entry in dates:
            if not isinstance(date_entry, dict):
                raise forms.ValidationError(
                    "Each date entry must be a dictionary."
                )
            if 'start_date' not in date_entry or 'end_date' not in date_entry:
                raise forms.ValidationError(
                    "Each date entry must contain 'start_date' and 'end_date'."
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
                    "Invalid date format. Use YYYY-MM-DD."
                )
            if start_date > end_date:
                raise forms.ValidationError(
                    "Start date cannot be after end date."
                )
        return dates


class CaravanImageForm(forms.ModelForm):
    class Meta:
        model = CaravanImage
        fields = ['image']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'name', 'email', 'phone_number', 'start_date', 'end_date',
            'message'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        self.caravan = kwargs.pop('caravan', None)
        super().__init__(*args, **kwargs)
        if self.caravan:
            self.instance.caravan = self.caravan

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        # Ensure the Booking instance has a caravan before accessing it
        if not self.instance.caravan_id:
            raise forms.ValidationError(
                "This booking does not have an associated caravan."
            )

        # Now safe to access
        caravan = self.instance.caravan

        if start_date and end_date:
            if start_date > end_date:
                raise forms.ValidationError(
                    "End date must be after start date."
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
                    "The caravan is not available for the selected dates."
                )

        return cleaned_data


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3})
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reply']
        widgets = {
            'reply': forms.Textarea(attrs={'rows': 3})
        }
