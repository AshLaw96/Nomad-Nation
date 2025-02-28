from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    """
    Represents a user's profile containing personal details and preferences.
    Attributes:
        - user (OneToOneField): Links to the User model.
        - profile_pic (ImageField): Stores the user's profile picture.
        - bio (TextField): A short biography about the user.
        - phone_number (CharField): The user's contact number.
        - language (CharField): Stores the user's preferred language.
        - appearance (CharField): Stores the user's theme preference
          (light/dark).
        - currency (CharField): The preferred currency for transactions.
        - notifications (BooleanField): Determines if notifications are
          enabled.
    """
    LANGUAGE_CHOICES = [
        ('en', _('English')),
        ('es', _('Spanish')),
        ('fr', _('French')),
        ('de', _('German')),
        ('it', _('Italian')),
        ('pt', _('Portuguese')),
        ('ru', _('Russian')),
        ('zh', _('Chinese')),
        ('ja', _('Japanese')),
        ('hi', _('Hindi')),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile'
    )
    phone_number = models.CharField(max_length=15, blank=True)
    language = models.CharField(
        max_length=2, choices=LANGUAGE_CHOICES, default='en'
    )
    appearance = models.CharField(
        max_length=20,
        choices=[('light', 'Light'), ('dark', 'Dark')],
        default='light'
    )
    currency = models.CharField(max_length=3, default='GBP')
    notifications = models.BooleanField(default=True)

    def __str__(self):
        """
        Returns the username of the associated user.
        """
        return self.user.username


class Notification(models.Model):
    """
    Stores notifications for users about various actions.
    Attributes:
        - user (ForeignKey): The recipient of the notification.
        - message (TextField): The content of the notification.
        - type (CharField): The type of notification (e.g., review, booking).
        - booking (ForeignKey): Links to a booking (if applicable).
        - caravan (ForeignKey): Links to a caravan (if applicable).
        - review (ForeignKey): Links to a review (if applicable).
        - is_read (BooleanField): Indicates if the notification has been read.
        - created_at (DateTimeField): Timestamp of when the notification was
          created.
        - created_by (ForeignKey): The user who triggered the notification.
        - related_object_id (PositiveIntegerField): Stores the ID of the
          related object.
    """
    REVIEW = 'review'
    REPLY = 'reply_to_review'
    BOOKING_REQUEST = 'booking_request'
    BOOKING_ACCEPTED = 'booking_accepted'
    BOOKING_DECLINED = 'booking_declined'
    BOOKING_MODIFIED_REQUEST = 'booking_modified_request'
    CONTACT_FORM = 'contact_form_message'

    NOTIFICATION_TYPE_CHOICES = [
        (REVIEW, _('Review')),
        (REPLY, _('Reply to Review')),
        (BOOKING_REQUEST, _('Booking Request')),
        (BOOKING_ACCEPTED, _('Booking Accepted')),
        (BOOKING_DECLINED, _('Booking Declined')),
        (BOOKING_MODIFIED_REQUEST, _('Booking Modification Request')),
        (CONTACT_FORM, _('Contact Form Message')),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notifications'
    )
    message = models.TextField()
    type = models.CharField(
        max_length=50,
        choices=NOTIFICATION_TYPE_CHOICES
    )
    booking = models.ForeignKey(
        'listings.Booking',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notifications'
    )
    caravan = models.ForeignKey(
        'listings.Caravan',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notifications'
    )
    review = models.ForeignKey(
        'listings.Review',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notifications'
    )

    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notifications_created'
    )

    related_object_id = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        """
        Returns a formatted notification message for the user.
        """
        return (
            _('Notification for ') + f'{self.user.username} - {self.message}'
        )

    def mark_as_read(self):
        """
        Marks the notification as read.
        """
        self.is_read = True
        self.save()


class PaymentDetails(models.Model):
    """
    Stores payment details associated with a user.
    Attributes:
        - user (ForeignKey): The user associated with the payment details.
        - card_last_four (CharField): Stores the last four digits of the card.
        - payment_method (CharField): The type of payment method used.
        - billing_address (TextField): The billing address for the payment.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='payment_details'
    )
    card_last_four = models.CharField(max_length=4)
    payment_method = models.CharField(max_length=50)
    billing_address = models.TextField()

    def __str__(self):
        """
        Returns a masked card display with the payment method.
        """
        return f"{self.payment_method} **** **** **** {self.card_last_four}"


class PrivacySettings(models.Model):
    """
    Stores user privacy preferences.
    Attributes:
        - user (OneToOneField): The user linked to these privacy settings.
        - data_sharing_enabled (BooleanField): Whether the user has enabled
          data sharing.
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='privacy_settings'
    )
    data_sharing_enabled = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a readable string for the privacy settings.
        """
        return _('Privacy settings for') + f' {self.user.username}'
