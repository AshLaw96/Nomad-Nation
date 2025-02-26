from django import forms
from allauth.account.forms import SignupForm
from .models import UserProfile


class CustomSignupForm(SignupForm):
    """
    Custom sign-up form extending the default SignupForm to include a user type
    selection.
    """
    user_type = forms.ChoiceField(
        choices=UserProfile.USER_TYPES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def save(self, request):
        """
        Saves the user instance and creates a corresponding UserProfile
        with the selected user type.

        Args:
            request: The HTTP request object.

        Returns:
            The newly created user instance.
        """
        # Save the user instance using the base SignupForm logic.
        user = super().save(request)
        UserProfile.objects.create(
            user=user,
            # Assign the selected user type.
            user_type=self.cleaned_data['user_type'],
        )
        # Return the created user instance.
        return user
