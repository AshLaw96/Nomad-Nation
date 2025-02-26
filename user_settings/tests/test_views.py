import json
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from user_settings.models import Notification, UserProfile


class AccountSettingsViewTest(TestCase):
    def setUp(self):
        """
        Set up the test environment for the AccountSettingsView tests.
        Initializes a client and creates a user. The user is logged in to
        ensure that authenticated requests can be made in the tests.
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="password"
        )
        self.client.login(username="testuser", password="password")

    def test_account_settings_view(self):
        """
        Test the account settings view for an authenticated user.
        This test verifies that the account settings page is accessible
        and renders the correct template.
        """
        response = self.client.get(reverse("account_settings"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "user_settings/account_settings.html"
        )


class EditPersonalDetailsViewTest(TestCase):
    def setUp(self):
        """
        Set up the test environment for the EditPersonalDetailsView tests.
        Initializes a client, creates a user, and logs them in. Additionally,
        a UserProfile is created for the user to store their personal details.
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            password="password",
            email="test@example.com"
        )
        self.client.login(username="testuser", password="password")

        # Ensure a UserProfile exists for the user
        self.user_profile = UserProfile.objects.create(
            user=self.user, phone_number="123456789"
        )

    def test_edit_personal_details_post(self):
        """
        Test editing personal details via a POST request.
        This test verifies that a POST request with updated personal
        details (username, email, and phone number) updates the user's data
        correctly and redirects to the appropriate page.
        """
        response = self.client.post(reverse("edit_personal_details"), {
            "username": "updateduser",
            "email": "updated@example.com",
            "phone_number": "987654321"
        })

        self.user.refresh_from_db()
        self.user_profile.refresh_from_db()

        # Redirect after successful update
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.user.username, "updateduser")
        self.assertEqual(self.user.email, "updated@example.com")
        self.assertEqual(self.user_profile.phone_number, "987654321")


class GetNotificationsViewTest(TestCase):
    def setUp(self):
        """
        Set up the test environment for the GetNotificationsView tests.
        Initializes a client, creates a user, and logs them in. A notification
        is also created for the user.
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="password"
        )
        self.client.login(username="testuser", password="password")
        Notification.objects.create(
            user=self.user,
            message="New notification",
            type="review"
        )

    def test_get_notifications(self):
        """
        Test retrieving notifications via a GET request.
        This test ensures that the `get_notifications` view returns the
        correct number of notifications and their details in the expected
        JSON format.
        """
        response = self.client.get(reverse("get_notifications"))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {
            "count": 1,
            "notifications": [{
                "message": "New notification",
                "type": "Review",
                "created_at": Notification.objects.first().created_at.strftime(
                    '%Y-%m-%d %H:%M:%S'
                ),
                "link": "#"
            }]
        })


class EditPaymentDetailsViewTest(TestCase):
    def setUp(self):
        """
        Set up the test environment for the EditPaymentDetailsView tests.
        Initializes a client and creates a user. The user is logged in
        to ensure authenticated requests can be made.
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="password"
        )
        self.client.login(username="testuser", password="password")

    def test_edit_payment_details(self):
        """
        Test editing payment details via a POST request.
        This test verifies that a POST request with updated payment details
        (card last four digits, payment method, billing address) correctly
        updates the user's payment information and returns a success response.
        """
        response = self.client.post(
            reverse("edit_payment_details"),
            json.dumps({
                "card_last_four": "5678",
                "payment_method": "MasterCard",
                "billing_address": "456 Avenue"
            }),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {
            "success": True,
            "payment_method": "MasterCard",
            "card_last_four": "5678"
        })


class DeleteProfileViewTest(TestCase):
    def setUp(self):
        """
        Set up the test environment for the DeleteProfileView tests.
        Initializes a client and creates a user. The user is logged in
        to ensure authenticated requests can be made.
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="password"
        )
        self.client.login(username="testuser", password="password")

    def test_delete_profile(self):
        """
        Test deleting a user profile.
        This test verifies that when a POST request is sent to delete the
        profile, the user is redirected to the homepage and the profile is
        deleted.
        """
        response = self.client.post(reverse("delete_profile"))
        self.assertRedirects(response, reverse("homepage"))
        self.assertFalse(User.objects.filter(username="testuser").exists())
