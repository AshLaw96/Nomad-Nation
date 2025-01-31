from django.contrib import admin
from .models import Caravan, Amenity, Availability


class CaravanAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = (
        'title', 'owner', 'location',
        'price_per_night', 'is_available'
    )

    fields = (
        'owner', 'title', 'description', 'berth',
        'price_per_night', 'location', 'amenities'
    )


admin.site.register(Caravan, CaravanAdmin)
admin.site.register(Amenity)
admin.site.register(Availability)
