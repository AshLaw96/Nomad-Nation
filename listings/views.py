from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Caravan, Amenity, Availability, CaravanImage, Booking, \
    Review, Reply
from .forms import CaravanForm, BookingForm, ReviewForm, ReplyForm
from user_settings.currency import convert_currency


@login_required
def listings_view(request):
    """
    Displays all caravans owned by the logged-in user.
    Includes search and filtering functionality.
    """
    user_type = request.user.profile.user_type
    user_currency = request.session.get('currency', 'GBP')

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

    # Convert price for each caravan
    for caravan in caravans:
        caravan.converted_price = convert_currency(
            caravan.price_per_night, user_currency
        )

    # Check if each caravan is favourited by the current user
    for caravan in caravans:
        caravan.is_favourite = caravan.favourites.filter(
            id=request.user.id).exists()

    context = {
        'caravans': caravans,
        'user_type': user_type,
        'username': request.user.username,
        'amenities': Amenity.objects.all(),
        'selected_amenities': filter_amenities,
        'user_currency': user_currency,
    }
    return render(request, 'listings/listing_page.html', context)


@csrf_exempt
@require_POST
@login_required
def toggle_favourite(request, caravan_id):
    try:
        caravan = get_object_or_404(Caravan, pk=caravan_id)
        if request.user in caravan.favourites.all():
            caravan.favourites.remove(request.user)
            is_favourite = False
        else:
            caravan.favourites.add(request.user)
            is_favourite = True
        return JsonResponse({'success': True, 'is_favourite': is_favourite})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


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

    # Ensure the caravan context is passed
    caravan = None
    if bookings.exists():
        caravan = bookings.first().caravan

    # Add a flag to each booking indicating if it can be modified
    for booking in upcoming_bookings:
        booking.can_modify = (booking.start_date - today).days > 7

    form = BookingForm()

    return render(request, 'listings/booking.html', {
        'pending_bookings': pending_bookings,
        'upcoming_bookings': upcoming_bookings,
        'previous_bookings': previous_bookings,
        'user_type': user_type,
        'caravan': caravan,
        'form': form,
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
                return redirect("booking_page")
        else:
            messages.error(
                request, "There was an error with your booking request."
            )
    else:
        form = BookingForm()

    return render(
        request,
        "listings/booking.html",
        {
            "form": form,
            "caravan": caravan,
            "pending_bookings": Booking.objects.filter(status='pending'),
            "upcoming_bookings": Booking.objects.filter(
                status='accepted',
                start_date__gte=timezone.now().date()
            ),
            "previous_bookings": Booking.objects.filter(
                status='accepted', end_date__lt=timezone.now().date()
            ),
            "user_type": request.user.profile.user_type,
        }
    )


@login_required
def booking_view(request, caravan_id):
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

    # Add a flag to each booking indicating if it can be modified
    for booking in upcoming_bookings:
        booking.can_modify = (booking.start_date - today).days > 7

    return render(request, 'listings/booking.html', {
        'caravan': caravan,
        'pending_bookings': pending_bookings,
        'upcoming_bookings': upcoming_bookings,
        'previous_bookings': previous_bookings,
        'user_type': user_type,
        'has_pending': pending_bookings.exists(),
        'has_upcoming': upcoming_bookings.exists(),
        'has_previous': previous_bookings.exists(),
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
        return redirect("booking_view", caravan_id=booking.caravan.id)

    return redirect("booking_view", caravan_id=booking.caravan.id)


@login_required
def modify_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)

    if request.method == "POST":
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        # Update booking dates
        booking.start_date = start_date
        booking.end_date = end_date
        # Set status to pending for owner approval
        booking.status = "pending"
        booking.save()

        messages.success(
            request, "Booking modification request sent to the owner."
        )
        return redirect("booking_view", caravan_id=booking.caravan.id)

    return redirect("booking_view", caravan_id=booking.caravan.id)


@login_required
def submit_review(request, caravan_id):
    caravan = get_object_or_404(Caravan, pk=caravan_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.caravan = caravan
            review.customer = request.user
            review.save()

            messages.success(request, "Review submitted successfully!")

            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({"success": True})

            return redirect("listings")

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({"errors": form.errors}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)


@login_required
def approve_review(request, review_id):
    review = get_object_or_404(
        Review, pk=review_id, caravan__owner=request.user
    )
    if request.user == review.caravan.owner:
        review.approved = True
        review.save()
        messages.success(request, "Review approved!")
    return redirect("listings")


@login_required
def submit_reply(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.review = review
            reply.owner = request.user
            reply.save()
            messages.success(request, "Reply submitted successfully!")
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({"success": True})
            return redirect("listings")
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({"errors": form.errors}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)


@login_required
def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk, customer=request.user)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review edited successfully!")
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({"success": True})
            return redirect("listings")
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({"errors": form.errors}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)


def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk, customer=request.user)
    review.delete()
    messages.success(request, "Review deleted successfully!")
    return JsonResponse({"success": True})


@login_required
def edit_reply(request, pk):
    reply = get_object_or_404(
        Reply, pk=pk, review__caravan__owner=request.user
    )
    if request.method == "POST":
        form = ReplyForm(request.POST, instance=reply)
        if form.is_valid():
            form.save()
            messages.success(request, "Reply edited successfully!")
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({"success": True})
            return redirect("listings")
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({"errors": form.errors}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)


@login_required
def delete_reply(request, pk):
    reply = get_object_or_404(
        Reply, pk=pk, review__caravan__owner=request.user
    )
    reply.delete()
    messages.success(request, "Reply deleted successfully!")
    return JsonResponse({"success": True})
