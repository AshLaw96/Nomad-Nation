from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.translation import activate
from user_settings.models import (
    UserProfile,
    Notification,
    PaymentDetails,
    PrivacySettings,
)


class UserProfileModelTest(TestCase):
    def setUp(self):
        """
        Set up the test environment for the UserProfile model tests.
        Initializes a user and a corresponding profile with a phone number.
        This method is called before each test case to ensure that a user
        profile is available for testing.
        """
        self.user = User.objects.create_user(
            username="testuser", password="password"
        )
        self.profile = UserProfile.objects.create(
            user=self.user, phone_number="123456789"
        )

    def test_profile_creation(self):
        """
        Test the correct creation of a user profile.
        This test checks that a user profile is properly created with the
        correct user and phone number fields.
        """
        self.assertEqual(self.profile.user.username, "testuser")
        self.assertEqual(self.profile.phone_number, "123456789")

    def test_profile_str_representation(self):
        """
        Test the string representation of the user profile.
        This test checks if the string representation of the profile
        returns the correct username.
        """
        self.assertEqual(str(self.profile), "testuser")


class NotificationModelTest(TestCase):
    def setUp(self):
        """
        Set up the test environment for the Notification model tests.
        Initializes a user and a corresponding notification. This method is
        called before each test case to ensure that a notification is
        available for testing.
        """
        self.user = User.objects.create_user(
            username="testuser", password="password"
        )
        self.notification = Notification.objects.create(
            user=self.user, message="Test notification", type="review"
        )

    def test_notification_creation(self):
        """
        Test the correct creation of a notification.
        This test checks that a notification is created with the correct
        user and message fields.
        """
        self.assertEqual(self.notification.user.username, "testuser")
        self.assertEqual(self.notification.message, "Test notification")

    def test_mark_as_read(self):
        """
        Test the functionality of marking a notification as read.
        This test ensures that calling the `mark_as_read` method correctly
        updates the notification's `is_read` status.
        """
        self.notification.mark_as_read()
        self.assertTrue(self.notification.is_read)


class PaymentDetailsModelTest(TestCase):
    def setUp(self):
        """
        Set up the test environment for the PaymentDetails model tests.
        Initializes a user and corresponding payment details. This method is
        called before each test case to ensure that payment details are
        available for testing.
        """
        self.user = User.objects.create_user(
            username="testuser", password="password"
        )
        self.payment_details = PaymentDetails.objects.create(
            user=self.user, card_last_four="1234", payment_method="Visa",
            billing_address="123 Street"
        )

    def test_payment_details_creation(self):
        """
        Test the correct creation of payment details.
        This test checks that payment details are created with the correct
        fields: last four digits of the card, payment method, and billing
        address.
        """
        self.assertEqual(self.payment_details.card_last_four, "1234")
        self.assertEqual(self.payment_details.payment_method, "Visa")
        self.assertEqual(self.payment_details.billing_address, "123 Street")

    def test_payment_details_str_representation(self):
        """
        Test the string representation of the payment details.
        This test checks if the string representation of the payment details
        correctly formats the payment method and card number (last four
        digits).
        """
        self.assertEqual(str(self.payment_details), "Visa **** **** **** 1234")


class PrivacySettingsModelTest(TestCase):
    def setUp(self):
        """
        Set up the test environment for the PrivacySettings model tests.
        Initializes a user and corresponding privacy settings. This method
        is called before each test case to ensure privacy settings are
        available for testing.
        """
        self.user = User.objects.create_user(
            username="testuser", password="password"
        )
        self.privacy_settings = PrivacySettings.objects.create(
            user=self.user, data_sharing_enabled=True
        )

    def test_privacy_settings_creation(self):
        """
        Test the correct creation of privacy settings.
        This test checks that privacy settings are created with the correct
        value for data sharing (enabled).
        """
        self.assertTrue(self.privacy_settings.data_sharing_enabled)

    def test_privacy_settings_str_representation(self):
        """
        Test the string representation of the privacy settings.
        This test ensures that the string representation of the privacy
        settings includes the user's username and the correct privacy
        settings text.
        """
        # Force English locale
        activate('en')
        self.assertEqual(
            str(self.privacy_settings),
            f"Privacy settings for {self.user.username}"
        )
