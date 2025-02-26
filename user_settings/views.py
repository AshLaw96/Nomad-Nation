from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from django.utils import translation
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from django.utils.translation import gettext_lazy as _
from .models import UserProfile, PaymentDetails, PrivacySettings, Notification


@login_required
def account_settings(request):
    """
    View for displaying user account settings, including:
    - User profile information
    - Payment details
    - Privacy settings
    Ensures UserProfile and PrivacySettings exist before rendering.
    """
    user_profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )
    payment_details = PaymentDetails.objects.filter(
        user=request.user
    )
    privacy_settings, created = PrivacySettings.objects.get_or_create(
        user=request.user
    )

    context = {
        'user_profile': user_profile,
        'payment_details': payment_details,
        'privacy_settings': privacy_settings
    }
    return render(request, 'user_settings/account_settings.html', context)


@login_required
def edit_personal_details(request):
    """
    View to handle editing of personal details such as:
    - Username
    - Email
    - Phone number (stored in UserProfile)
    Updates user data and redirects to account settings upon success.
    """
    if request.method == 'POST':
        user = request.user
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()

        user_profile = UserProfile.objects.get(user=user)
        user_profile.phone_number = request.POST['phone_number']
        user_profile.save()

        messages.success(request, _('Personal details updated successfully.'))
        return redirect('account_settings')


@login_required
def edit_preferences(request):
    """
    View to update user preferences including:
    - Language
    - Currency
    - Appearance mode (light/dark)
    - Notification preferences
    Updates the session with language and currency settings and returns
    JSON response.
    """
    if request.method == "POST":
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.language = request.POST.get(
            "language", user_profile.language
        )
        user_profile.currency = request.POST.get("currency", "GBP")
        user_profile.appearance = request.POST.get(
            "appearance", user_profile.appearance
        )
        user_profile.notifications = "notifications" in request.POST
        user_profile.save()

        # Activate the selected language
        translation.activate(user_profile.language)
        request.session[settings.LANGUAGE_COOKIE_NAME] = user_profile.language

        # Store the currency preference in the session
        request.session["currency"] = user_profile.currency

        return JsonResponse({
            "success": True,
            "language": user_profile.language,
            "language_display": user_profile.get_language_display(),
            "currency": user_profile.currency,
            "appearance": user_profile.appearance,
            "notifications_enabled": user_profile.notifications,
        })

    return JsonResponse({"success": False, "error": _("Invalid request")})


def convert_price(request):
    """
    View to convert a given amount to the selected currency.
    The request should include:
    - amount: The numeric value to be converted
    - currency: The target currency (defaults to GBP)
    Returns a JSON response with the converted price.
    """
    amount = float(request.GET.get('amount', 0))
    currency = request.GET.get('currency', 'GBP')
    converted_price = convert_price(amount, currency)

    return JsonResponse({'converted_price': converted_price})


@login_required
def get_notifications(request):
    """
    Fetches all unread notifications for the logged-in user.
    Returns a JSON response containing:
    - Notification count
    - List of notifications with message, type, timestamp, and relevant links.
    """
    user = request.user
    notifications = Notification.objects.filter(user=user, is_read=False)
    notifications_list = []

    for n in notifications:
        # Default if no link is available
        link = "#"

        if n.type == "review" and n.review:
            # reviews on listings page
            link = reverse("listings") + f"#review-{n.review.id}"
        elif n.type == "review_reply" and n.review:
            link = reverse("listings") + f"#review-{n.related_object.id}"
        elif n.type == "booking_request":
            link = reverse(
                "manage_booking", kwargs={"booking_id": n.booking.id}
            )
        elif n.type == "booking_accepted":
            link = reverse(
                    "booking_view", kwargs={"caravan_id": n.caravan.id}
                )
        elif n.type == "booking_declined":
            link = reverse(
                "booking_view", kwargs={"caravan_id": n.caravan.id}
            )
        elif n.type == "booking_modified_request":
            link = reverse(
                "booking_view", kwargs={"caravan_id": n.caravan.id}
            )
        elif n.type == "contact_form_message":
            link = reverse("contact")

        notifications_list.append({
            'message': n.message,
            'type': n.get_type_display(),
            'created_at': n.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            # Include link in response
            'link': link,
        })

    return JsonResponse({
        'count': notifications.count(),
        'notifications': notifications_list
    })


@login_required
@require_POST
def mark_notifications_read(request):
    """
    Marks all unread notifications as read for the logged-in user.
    Returns a JSON response confirming success.
    """
    Notification.objects.filter(
        user=request.user, is_read=False
    ).update(is_read=True)
    return JsonResponse({'success': True})


@login_required
def edit_payment_details(request):
    """
    Updates a user's payment details.
    - Parses JSON data from request
    - Validates card last four digits
    - Saves new payment details for the user
    Returns a JSON response confirming success or error message.
    """
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'error': _('Invalid JSON format.')
            })

        card_last_four = data.get('card_last_four', '')

        # Ensure card last four digits are exactly 4 numbers
        if not card_last_four.isdigit() or len(card_last_four) != 4:
            return JsonResponse({
                'success': False,
                'error': _('Invalid card number format.')
            })

        payment_details, created = PaymentDetails.objects.get_or_create(
            user=request.user
        )
        payment_details.payment_method = data.get('payment_method', '')
        payment_details.card_last_four = card_last_four
        payment_details.billing_address = data.get('billing_address', '')
        payment_details.save()

        return JsonResponse({
            'success': True,
            'payment_method': payment_details.payment_method,
            'card_last_four': payment_details.card_last_four,
        })

    return JsonResponse({'success': False})


@login_required
def delete_profile(request):
    """
    Allows a user to delete their profile.
    - Upon confirmation (POST request), the user's account is deleted.
    - Logs out the user and redirects to the homepage.
    """
    if request.method == "POST":
        user = request.user
        user.delete()
        # Log out the user after deletion
        logout(request)
        messages.success(
            request, _("Your profile has been deleted successfully.")
        )
        # Redirect to homepage after deletion
        return redirect("homepage")

    return render(request, "main/delete_profile.html")
