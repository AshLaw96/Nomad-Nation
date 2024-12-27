from django import forms
from .models import ContactMessage
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['recipient', 'message']  # Add recipient field

    def __init__(self, *args, **kwargs):
        # Capture the user (passed from the view)
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Filter recipient choices based on user type
        if self.user and self.user.is_authenticated:
            # Authenticated users: Show only customers or caravan owners
            self.fields['recipient'].queryset = User.objects.exclude(is_superuser=True)
        else:
            # Guest users: Show only admin
            self.fields['recipient'].queryset = User.objects.filter(is_superuser=True)
