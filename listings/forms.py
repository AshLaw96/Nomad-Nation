import json
from django import forms
from datetime import datetime
from .models import Caravan, Amenity, CaravanImage


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
