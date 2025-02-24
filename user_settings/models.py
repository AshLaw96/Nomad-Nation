from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
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
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    bio = models.TextField(blank=True)
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
        return self.user.username


class Notification(models.Model):
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
        return (
            _('Notification for ') + f'{self.user.username} - {self.message}'
        )

    def mark_as_read(self):
        self.is_read = True
        self.save()


class PaymentDetails(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='payment_details'
    )
    card_last_four = models.CharField(max_length=4)
    payment_method = models.CharField(max_length=50)
    billing_address = models.TextField()

    def __str__(self):
        return f"{self.payment_method} **** **** **** {self.card_last_four}"


class PrivacySettings(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='privacy_settings'
    )
    data_sharing_enabled = models.BooleanField(default=False)

    def __str__(self):
        return _('Privacy settings for') + f' {self.user.username}'
