from django.contrib import admin
from .models import UserProfile, Notification, PaymentDetails, PrivacySettings


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for User Profiles
    """
    list_display = (
        'user', 'phone_number', 'language', 'appearance',
        'currency', 'notifications'
    )
    search_fields = ('user__username', 'phone_number')
    list_filter = ('language', 'appearance', 'notifications')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """
    Admin configuration for Notifications
    """
    list_display = (
        'user', 'message', 'type', 'is_read', 'created_at', 'created_by'
    )
    list_filter = ('type', 'is_read', 'created_at')
    search_fields = ('user__username', 'message')
    readonly_fields = ('created_at',)
    # Prevents modifying timestamp manually
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        """
        Mark selected notifications as read
        """
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected notifications as read"


@admin.register(PaymentDetails)
class PaymentDetailsAdmin(admin.ModelAdmin):
    """
    Admin configuration for Payment Details
    """
    list_display = ('user', 'payment_method', 'card_last_four')
    search_fields = ('user__username', 'card_last_four')
    list_filter = ('payment_method',)


@admin.register(PrivacySettings)
class PrivacySettingsAdmin(admin.ModelAdmin):
    """
    Admin configuration for Privacy Settings
    """
    list_display = (
        'user', 'data_sharing_enabled'
    )
    list_filter = (
        'data_sharing_enabled',
    )
    search_fields = ('user__username',)
