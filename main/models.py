from django.db import models
from django.contrib.auth.models import User


class ContactMessage(models.Model):
    """
    Represents a private message sent between users.
    Messages can be sent by authenticated users or guests.
    """
    sender = models.ForeignKey(
        User,
        # If the sender is deleted, keep the message but set sender to NULL
        on_delete=models.SET_NULL,
        # Allows sender to be NULL (e.g., for guest messages)
        null=True,
        # Allows form submissions without a sender
        blank=True,
        # Reverse relation for accessing messages sent by a user
        related_name='message_sent'
    )
    recipient = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='messages_received'
    )
    # Subject of the message (max 200 characters)
    subject = models.CharField(max_length=200)
    # The body of the message
    message = models.TextField()
    # Timestamp when the message was sent (set automatically)
    sent_at = models.DateTimeField(auto_now_add=True)
    # Tracks whether the recipient has read the message
    is_read = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a human-readable string representation of the message.
        Shows sender and recipient usernames (or placeholders if missing),
        along with the subject and timestamp.
        """
        sender_name = (
            self.sender.username if self.sender else ("Guest")
        )
        recipient_name = (
            self.recipient.username if self.recipient else ("Unknown")
        )
        return (
            f"Message from {sender_name} to {recipient_name} - {self.subject} "
            f"({self.sent_at.strftime('%Y-%m-%d %H:%M:%S')})"
        )
