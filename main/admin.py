from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Admin configuration for ContactMessage.
    """
    # Columns in the admin panel
    list_display = ("sender", "recipient", "subject", "sent_at", "is_read")
    # Searchable fields
    search_fields = (
        "sender__username",
        "recipient__username",
        "subject",
        "message",
    )
    # Filters for read/unread and date
    list_filter = ("is_read", "sent_at")
    # Show newest messages first
    ordering = ("-sent_at",)
    # Prevent modification of the sent timestamp
    readonly_fields = ("sent_at",)
