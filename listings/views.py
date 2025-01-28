from django.contrib.auth.decorators import login_required
from .models import Caravan, Amenity, Availability, CaravanImage

@login_required
def listings_view(request):
    """
    Displays all caravans owned by the logged-in user.
    """
    user_type = request.user.profile.user_type
    if user_type == 'owner':
        caravans = Caravan.objects.filter(owner=request.user).prefetch_related('amenities', 'images', 'availabilities')
    else:
        caravans = Caravan.objects.all().prefetch_related('amenities', 'images', 'availabilities')

    context = {
        'caravans': caravans,
        'user_type': user_type,
        'username': request.user.username,
    }
    return render(request, 'listings/listing_page.html', context)

