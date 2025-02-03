from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone
from .models import Caravan, Amenity, Availability, CaravanImage, Booking
from .forms import CaravanForm, BookingForm


@login_required
def listings_view(request):
    """
    Displays all caravans owned by the logged-in user.
    Includes search and filtering functionality.
    """
    user_type = request.user.profile.user_type

    if user_type == 'owner':
        caravans = Caravan.objects.filter(owner=request.user)
    else:
        caravans = Caravan.objects.all()

    # Search Functionality
    search_query = request.GET.get('search', '')
    if search_query:
        caravans = caravans.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(location__icontains=search_query)
        )
    # Filter Functionality
    filter_berth = request.GET.get('berth', '')
    filter_location = request.GET.get('location', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    available_from = request.GET.get('available_from', '')
    available_to = request.GET.get('available_to', '')
    filter_amenities = request.GET.getlist('amenities', [])

    if filter_berth:
        caravans = caravans.filter(berth=filter_berth)
    if filter_location:
        caravans = caravans.filter(location__icontains=filter_location)
    if min_price:
        caravans = caravans.filter(price_per_night__gte=min_price)
    if max_price:
        caravans = caravans.filter(price_per_night__lte=max_price)
    if available_from:
        caravans = caravans.filter(
            availabilities__start_date__gte=available_from
        )
    if available_to:
        caravans = caravans.filter(availabilities__end_date__lte=available_to)
    if filter_amenities:
        caravans = caravans.filter(
            amenities__id__in=filter_amenities
        ).distinct()

    caravans = caravans.prefetch_related(
        'amenities', 'images', 'availabilities'
    )
    context = {
        'caravans': caravans,
        'user_type': user_type,
        'username': request.user.username,
        'amenities': Amenity.objects.all(),
        'selected_amenities': filter_amenities,
    }
    return render(request, 'listings/listing_page.html', context)


@login_required
def add_caravan(request):
    if request.method == 'POST':
        form = CaravanForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            caravan = form.save(commit=False)
            caravan.owner = request.user
            caravan.save()
            # Save ManyToMany field
            form.save_m2m()
            # Handle multiple amenities
            for key, value in request.POST.items():
                if key.startswith('extra_amenity_') and value:
                    amenity_obj, created = Amenity.objects.get_or_create(
                        name=value, owner=request.user
                    )
                    caravan.amenities.add(amenity_obj)
            # Handle availability
            available_dates_data = form.cleaned_data.get('available_dates', [])
            for date_entry in available_dates_data:
                Availability.objects.create(
                    caravan=caravan,
                    start_date=date_entry['start_date'],
                    end_date=date_entry['end_date']
                )
            # Handle multiple images
            for image in request.FILES.getlist('images'):
                CaravanImage.objects.create(caravan=caravan, image=image)
            return redirect('listings')
    else:
        form = CaravanForm(user=request.user)
    return render(request, 'listings/add_caravan.html', {'form': form})


@login_required
def edit_caravan(request, slug):
    caravan = get_object_or_404(
        Caravan,
        slug=slug,
        owner=request.user
    )
    if request.method == "POST":
        form = CaravanForm(
            request.POST,
            request.FILES,
            instance=caravan,
            user=request.user
        )
        if form.is_valid():
            caravan = form.save(commit=False)
            caravan.save()
            # Save ManyToMany field
            form.save_m2m()
            # Handle multiple amenities
            for key, value in request.POST.items():
                if key.startswith('extra_amenity_') and value:
                    amenity_obj, created = Amenity.objects.get_or_create(
                        name=value, owner=request.user
                    )
                    caravan.amenities.add(amenity_obj)
            # Handle multiple images
            for image in request.FILES.getlist('images'):
                CaravanImage.objects.create(caravan=caravan, image=image)
            return redirect('listings')
    else:
        form = CaravanForm(instance=caravan, user=request.user)
    return render(request, 'listings/add_caravan.html', {'form': form})


@login_required
def delete_caravan(request, pk):
    caravan = get_object_or_404(Caravan, pk=pk, owner=request.user)
    if request.method == "POST":
        caravan.delete()
        return redirect('listings')
    # Redirects to listing page if not a POST request
    return redirect('listings')


@login_required
def booking_page_view(request):
    """
    Displays all bookings for the logged-in user.
    Owners see all bookings for their caravans,
    while customers see their own bookings.
    """
    user = request.user
    user_type = user.profile.user_type
    today = timezone.now().date()

    # Fetch bookings based on user type
    if user_type == 'owner':
        bookings = Booking.objects.filter(caravan__owner=user)
    else:
        bookings = Booking.objects.filter(customer=user)

    # Split bookings into categories
    pending_bookings = bookings.filter(status='pending')
    upcoming_bookings = bookings.filter(
        status='accepted', start_date__gte=today
    )
    previous_bookings = bookings.filter(status='accepted', end_date__lt=today)

    return render(request, 'listings/booking.html', {
        'pending_bookings': pending_bookings,
        'upcoming_bookings': upcoming_bookings,
        'previous_bookings': previous_bookings,
        'user_type': user_type,
    })


@login_required
def book_caravan(request, caravan_id):
    caravan = get_object_or_404(Caravan, pk=caravan_id)

    if request.method == "POST":
        form = BookingForm(request.POST, caravan=caravan)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.caravan = caravan
            booking.customer = request.user

            # Check if the requested dates are available
            overlapping_bookings = Booking.objects.filter(
                caravan=caravan,
                status="accepted",
                start_date__lt=booking.end_date,
                end_date__gt=booking.start_date
            )

            if overlapping_bookings.exists():
                messages.error(
                    request,
                    "The caravan is not available for the selected dates."
                )
            else:
                # Save booking as "pending" to await owner's response
                booking.status = "pending"
                booking.save()
                messages.success(
                    request,
                    f"Booking request for {caravan.title} sent successfully "
                    f"to {caravan.owner.username}!"
                )
                return redirect("listings/booking.html")
        else:
            messages.error(
                request, "There was an error with your booking request."
            )
    else:
        form = BookingForm(caravan=caravan)

    return render(
        request,
        "listings/booking.html",
        {"form": form, "caravan": caravan}
    )


@login_required
def booking_view(request, caravan_id):
    print("booking_view executed")
    caravan = get_object_or_404(Caravan, id=caravan_id)
    user = request.user
    user_type = user.profile.user_type
    # Get today's date for comparison
    today = timezone.now().date()

    # Determine bookings based on user type (owner or customer)
    if user_type == 'owner' and user == caravan.owner:
        # Owner's bookings for this caravan
        bookings = Booking.objects.filter(caravan=caravan)
    else:
        # Customer's bookings
        bookings = Booking.objects.filter(customer=user)

    # Split bookings into Pending, Upcoming, and Previous
    pending_bookings = bookings.filter(status='pending')
    upcoming_bookings = bookings.filter(
        status='accepted', start_date__gte=today
    )
    previous_bookings = bookings.filter(status='accepted', end_date__lt=today)

    # Flags to show temporary sections
    has_pending = pending_bookings.exists()
    has_upcoming = upcoming_bookings.exists()
    has_previous = previous_bookings.exists()

    return render(request, 'listings/booking.html', {
        'caravan': caravan,
        'pending_bookings': pending_bookings,
        'upcoming_bookings': upcoming_bookings,
        'previous_bookings': previous_bookings,
        'user_type': user_type,
        'has_pending': has_pending,
        'has_upcoming': has_upcoming,
        'has_previous': has_previous,
    })


@login_required
def manage_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)

    if not booking.caravan:
        messages.error(request, "Booking has no associated caravan.")
        return redirect("listings")

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "accept":
            booking.status = "accepted"
            messages.success(request, "Booking accepted!")
        elif action == "decline":
            booking.status = "declined"
            messages.warning(request, "Booking declined.")

        booking.save()
        return redirect("listings")

    return redirect("listings")
