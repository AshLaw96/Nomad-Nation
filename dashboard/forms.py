from django import forms
from allauth.account.forms import SignupForm
from .models import UserProfile


class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(
        choices=UserProfile.USER_TYPES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def save(self, request):
        user = super().save(request)
        UserProfile.objects.create(
            user=user, user_type=self.cleaned_data['user_type']
        )
        return user
