from django.test import TestCase
from django.contrib.auth.models import User
from main.forms import ContactForm


class ContactFormTest(TestCase):
    def setUp(self):
        """
        Set up users for form testing.
        """
        self.user = User.objects.create_user(
            username="testuser", password="password"
        )
        self.admin = User.objects.create_superuser(
            username="admin", password="adminpass"
        )

        form = ContactForm(
            data={
                "recipient": self.user.id,
                "subject": "Test Message",
                "message": "This is a test message."
            },
            user=self.user,
        )
        self.assertTrue(form.is_valid())

    def test_contact_form_missing_fields(self):
        """
        Test form validation when required fields are missing.
        """
        # Use self.user from setUp
        form = ContactForm(data={}, user=self.user)

        self.assertFalse(form.is_valid())
        # Now recipient should be required
        self.assertIn("recipient", form.errors)
        self.assertIn("subject", form.errors)
        self.assertIn("message", form.errors)

    def test_contact_form_recipient_filter_authenticated(self):
        """
        Test recipient queryset for authenticated users (excludes superusers).
        """
        form = ContactForm(user=self.user)
        self.assertNotIn(self.admin, form.fields["recipient"].queryset)

    def test_contact_form_recipient_filter_guest(self):
        """
        Test recipient queryset for guests (only includes superusers).
        """
        form = ContactForm()
        self.assertIn(self.admin, form.fields["recipient"].queryset)
