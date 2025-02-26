from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import ContactMessage
from user_settings.models import Notification


class MainViewsTestCase(TestCase):
    def setUp(self):
        """
        Set up test users and messages.
        """
        self.superuser = User.objects.create_superuser(
            username="admin", email="admin@example.com", password="adminpass"
        )
        self.user1 = User.objects.create_user(
            username="user1", email="user1@example.com", password="password123"
        )
        self.user2 = User.objects.create_user(
            username="user2", email="user2@example.com", password="password123"
        )

        # Create a test message
        self.message = ContactMessage.objects.create(
            sender=self.user1,
            recipient=self.user2,
            subject="Test Subject",
            message="Test Message",
        )

    def test_homepage_loads_successfully(self):
        """
        Test if homepage loads correctly.
        """
        response = self.client.get(reverse("homepage"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/home.html")

    def test_contact_view_loads(self):
        """
        Test if contact page loads.
        """
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/contact.html")

    def test_authenticated_user_can_send_message(self):
        """
        Test if logged-in user can send a message.
        """
        self.client.login(username="user1", password="password123")

        response = self.client.post(
            reverse("contact"),
            {
                "recipient": self.user2.id,
                "subject": "New Message",
                "message": "Hello!",
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            ContactMessage.objects.filter(subject="New Message").exists()
        )

    def test_guest_user_can_send_message_to_admin(self):
        """
        Test if a guest can send a message to an admin.
        """
        response = self.client.post(
            reverse("contact"),
            {
                "recipient": self.superuser.id,
                "subject": "Guest Inquiry",
                "message": "Need help!",
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            ContactMessage.objects.filter(subject="Guest Inquiry").exists()
        )

    def test_message_sends_notification(self):
        """
        Test if sending a message creates a notification for the recipient.
        """
        self.client.login(username="user1", password="password123")
        self.client.post(
            reverse("contact"),
            {
                "recipient": self.user2.id,
                "subject": "Notification Test",
                "message": "Checking notifications!",
            },
            follow=True,
        )

        notification_exists = Notification.objects.filter(
            user=self.user2, message__contains="New contact message"
        ).exists()
        self.assertTrue(notification_exists)

    def test_contact_form_validation_errors(self):
        """
        Test that invalid form submission shows errors.
        """
        self.client.login(username="user1", password="password123")
        response = self.client.post(
            reverse("contact"),
            {
                # Missing recipient
                "recipient": "",
                "subject": "",
                "message": "",
            },
            follow=True,
        )

        self.assertContains(response, "This field is required.")

    def test_authenticated_user_can_delete_own_message(self):
        """
        Test if an authenticated user can delete their own received message.
        """
        self.client.login(username="user2", password="password123")
        response = self.client.post(
            reverse("delete_message", args=[self.message.id]), follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            ContactMessage.objects.filter(id=self.message.id).exists()
        )

    def test_user_cannot_delete_someone_elses_message(self):
        """
        Test if a user cannot delete another user's message.
        """
        # user1 is not the recipient
        self.client.login(username="user1", password="password123")

        response = self.client.post(
            reverse("delete_message", args=[self.message.id])
        )

        # Expecting a 403 Forbidden
        self.assertEqual(response.status_code, 403)
        # Message should still exist
        self.assertTrue(
            ContactMessage.objects.filter(id=self.message.id).exists()
        )
