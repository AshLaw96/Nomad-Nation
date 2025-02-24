from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class ContactMessage(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='message_sent'
    )
    recipient = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='messages_received'
    )
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        sender_name = (
            self.sender.username if self.sender else _("Guest")
        )
        recipient_name = (
            self.recipient.username if self.recipient else _("Unknown")
        )
        return _(
            _("Message from ") + f"{sender_name}"
            + _(" to") +
            f" {recipient_name} - "
            f"{self.subject} ({self.sent_at.strftime('%Y-%m-%d %H:%M:%S')})"
        )
