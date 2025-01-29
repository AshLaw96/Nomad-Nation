from django import forms
from django.contrib.auth.models import User
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['recipient', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        # Capture the user (passed from the view)
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Filter recipient choices based on user type
        if self.user and self.user.is_authenticated:
            # Authenticated users: Exclude superusers
            self.fields['recipient'].queryset = User.objects.exclude(
                is_superuser=True
            )
        else:
            # Guest users: Show only superusers
            self.fields['recipient'].queryset = User.objects.filter(
                is_superuser=True
            )
