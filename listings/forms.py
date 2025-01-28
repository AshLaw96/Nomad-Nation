from django import forms
from .models import Caravan, Availability, Amenity, CaravanImage


class CaravanForm(forms.ModelForm):
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
            'title', 'description','berth', 'amenities', 'location',
            'price_per_night', 'available_dates'
        ]
        widgets = {
            'amenities': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['amenities'].queryset = Amenity.objects.filter(owner=user)

