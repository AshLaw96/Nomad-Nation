from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # Display username & user type in the list
    list_display = ("user", "user_type")
    # Search by username & email
    search_fields = ("user__username", "user__email")
    # Filter by user type
    list_filter = ("user_type",)
    # Order by username
    ordering = ("user__username",)
    # Improves performance for large user lists
    autocomplete_fields = ("user",)
