from django.test import TestCase
from django.contrib.auth import get_user_model
from dashboard.models import UserProfile

User = get_user_model()


class UserProfileModelTests(TestCase):
    """
    Tests for the UserProfile model
    """

    def test_create_user_profile(self):
        """
        Test that a UserProfile is correctly linked to a User
        """
        user = User.objects.create_user(
            username="testuser", password="testpass"
        )
        profile = UserProfile.objects.create(user=user, user_type="customer")
        self.assertEqual(profile.user.username, "testuser")
        self.assertEqual(profile.user_type, "customer")
        self.assertEqual(str(profile), "testuser (customer)")
