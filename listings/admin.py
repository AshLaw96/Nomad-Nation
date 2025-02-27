from django.contrib import admin
from .models import (
    Caravan, Amenity, Availability, CaravanImage,
    Booking, Review, Reply
)


class CaravanImageInline(admin.TabularInline):
    """
    Allows images to be managed directly in the Caravan admin page.
    """
    model = CaravanImage
    # Show an empty slot for adding new images
    extra = 1


class AvailabilityInline(admin.TabularInline):
    """
    Allows availability periods to be managed inside Caravan admin.
    """
    model = Availability
    extra = 1


class CaravanAdmin(admin.ModelAdmin):
    """
    Admin panel customization for Caravan model.
    """
    list_display = (
        "title", "owner", "location",
        "price_per_night", "is_available"
    )
    search_fields = ("title", "owner__username", "location")
    list_filter = ("berth", "location", "price_per_night")
    # Add related objects
    inlines = [CaravanImageInline, AvailabilityInline]
    readonly_fields = ("is_available",)


class BookingAdmin(admin.ModelAdmin):
    """
    Admin panel customization for Booking model.
    """
    list_display = (
        "caravan", "customer", "start_date", "end_date", "status"
    )
    search_fields = ("caravan__title", "customer__username", "email")
    list_filter = ("status", "start_date", "end_date")
    ordering = ("-start_date",)


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin panel customization for Review model.
    """
    list_display = ("caravan", "customer", "rating", "approved", "created_at")
    search_fields = ("caravan__title", "customer__username", "comment")
    list_filter = ("approved", "rating")
    ordering = ("-created_at",)


class ReplyAdmin(admin.ModelAdmin):
    """
    Admin panel customization for Reply model.
    """
    list_display = ("review", "owner", "created_at")
    search_fields = ("review__caravan__title", "owner__username", "reply")
    ordering = ("-created_at",)


# Registering models
admin.site.register(Caravan, CaravanAdmin)
admin.site.register(Amenity)
admin.site.register(Availability)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Reply, ReplyAdmin)
