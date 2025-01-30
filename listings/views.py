from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Caravan, Amenity, Availability, CaravanImage, Booking
from django.contrib import messages
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
        caravans = caravans.filter(price__gte=min_price)
    if max_price:
        caravans = caravans.filter(price__lte=max_price)
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
def edit_caravan(request, pk):
    caravan = get_object_or_404(
        Caravan,
        pk=pk,
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
def book_caravan(request, caravan_id):
    caravan = get_object_or_404(Caravan, pk=caravan_id)

    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        customer_email = request.POST.get("customer_email")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        # Create a new booking request
        Booking.objects.create(
            caravan=caravan,
            customer=request.user,
            customer_name=customer_name,
            customer_email=customer_email,
            start_date=start_date,
            end_date=end_date,
            status="pending"
        )
        messages.success(request, "Booking request sent successfully!")
        return redirect("listings")

    return render(request, "book_caravan.html", {"caravan": caravan})


@login_required
def bookings_view(request):
    bookings = Booking.objects.filter(customer=request.user)
    return render(request, 'listings/booking.html', {'bookings': bookings})


@login_required
def booking_view(request, caravan_id):
    caravan = get_object_or_404(Caravan, id=caravan_id)
    user = request.user
    user_type = user.profile.user_type

    if request.method == 'POST':
        if 'action' in request.POST:
            # Handle accept/decline actions
            booking_id = request.POST.get('booking_id')
            action = request.POST.get('action')
            booking = get_object_or_404(Booking, id=booking_id)
            if action == 'accept':
                booking.status = 'accepted'
            elif action == 'decline':
                booking.status = 'declined'
            booking.save()
            return redirect('book_caravan', caravan_id=caravan_id)
        else:
            # Handle booking request submission
            form = BookingForm(request.POST)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.caravan = caravan
                booking.customer = user
                booking.save()
                return redirect('book_caravan', caravan_id=caravan_id)
    else:
        form = BookingForm()

    if user_type == 'owner' and user == caravan.owner:
        bookings = Booking.objects.filter(caravan=caravan)
        return render(request, 'listings/booking.html', {
            'caravan': caravan,
            'bookings': bookings,
            'user_type': user_type,
        })
    else:
        bookings = Booking.objects.filter(customer=user)
        return render(request, 'listings/booking.html', {
            'caravan': caravan,
            'form': form,
            'bookings': bookings,
            'user_type': user_type,
        })


@login_required
def manage_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)

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
