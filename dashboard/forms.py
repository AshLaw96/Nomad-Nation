from django import forms
from .models import CustomUser


class CustomUserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(
        choices=CustomUser.USER_TYPES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'user_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("form fields:", self.fields)

    def save(self, commit=True):
        user = super().save(commit=False)
        # Hash the password
        user.set_password(self.cleaned_data['password'])  
        if commit:
            user.save()
        return user
