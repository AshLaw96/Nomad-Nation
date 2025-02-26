from django import forms
from django.contrib.auth.models import User
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """
    A form for sending messages between users.
    Dynamically filters the recipient field based on the user's
    authentication status.
    """
    class Meta:
        # Specifies the model associated with this form
        model = ContactMessage
        fields = ['recipient', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        """
        Initializes the form, capturing the user instance and filtering
        recipient choices accordingly.
        - Authenticated users: Can send messages to all users except
          superusers.
        - Guest users: Can only send messages to superusers.
        """
        # Capture the user (passed from the view)
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Explicitly mark recipient as required
        self.fields["recipient"].required = True

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
