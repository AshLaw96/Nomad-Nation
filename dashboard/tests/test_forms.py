from django.test import TestCase
from django.contrib.auth import get_user_model
from dashboard.forms import CustomSignupForm

User = get_user_model()


class CustomSignupFormTests(TestCase):
    """
    Tests for the CustomSignupForm
    """

    def test_signup_form_valid(self):
        """
        Test that the form saves a user with a UserProfile
        """
        form_data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password1": "strongpassword123",
            "password2": "strongpassword123",
            "user_type": "owner",
        }
        form = CustomSignupForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save(self.client)
        self.assertEqual(user.username, "newuser")
        self.assertEqual(user.profile.user_type, "owner")
