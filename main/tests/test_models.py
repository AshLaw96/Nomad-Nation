from django.test import TestCase
from django.contrib.auth.models import User
from main.models import ContactMessage


class ContactMessageModelTest(TestCase):
    def setUp(self):
        """
        Set up users and a test message.
        """
        self.sender = User.objects.create_user(
            username="sender", password="pass"
        )
        self.recipient = User.objects.create_user(
            username="recipient", password="pass"
        )

        self.message = ContactMessage.objects.create(
            sender=self.sender,
            recipient=self.recipient,
            subject="Test Subject",
            message="This is a test message."
        )

    def test_contact_message_creation(self):
        """
        Test if ContactMessage is created correctly.
        """
        self.assertEqual(self.message.subject, "Test Subject")
        self.assertEqual(self.message.message, "This is a test message.")
        self.assertEqual(self.message.sender, self.sender)
        self.assertEqual(self.message.recipient, self.recipient)
        # Default should be False
        self.assertFalse(self.message.is_read)

    def test_contact_message_str_method(self):
        """
        Test the string representation of ContactMessage.
        """
        self.client.login(username="user1", password="testpass")

        expected_string = (
            f"Message from {self.sender.username} to {self.recipient.username}"
            f" - Test Subject "
            f"({self.message.sent_at.strftime('%Y-%m-%d %H:%M:%S')})"
        )
        self.assertEqual(expected_string, str(self.message))
