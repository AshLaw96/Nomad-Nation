from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.utils import translation
from django.http import JsonResponse
from .models import UserProfile, PaymentDetails, PrivacySettings


@login_required
def account_settings(request):
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
    if request.method == 'POST':
        user = request.user
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()

        user_profile = UserProfile.objects.get(user=user)
        user_profile.phone_number = request.POST['phone_number']
        user_profile.save()

        messages.success(request, 'Personal details updated successfully.')
        return redirect('account_settings')


@login_required
def edit_preferences(request):
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

    return JsonResponse({"success": False, "error": "Invalid request"})


def convert_price(request):
    amount = float(request.GET.get('amount', 0))
    currency = request.GET.get('currency', 'GBP')
    converted_price = convert_price(amount, currency)

    return JsonResponse({'converted_price': converted_price})


@login_required
def edit_payment_details(request):
    if request.method == 'POST':
        card_last_four = request.POST.get('card_last_four', '')

        # Ensure card last four digits are exactly 4 numbers
        if not card_last_four.isdigit() or len(card_last_four) != 4:
            return JsonResponse({
                'success': False,
                'error': 'Invalid card number format.'
            })

        payment_details, created = PaymentDetails.objects.get_or_create(
            user=request.user
        )
        payment_details.payment_method = request.POST.get('payment_method', '')
        payment_details.card_last_four = card_last_four
        payment_details.billing_address = request.POST.get(
            'billing_address', ''
        )
        payment_details.save()

        return JsonResponse({
            'success': True,
            'payment_method': payment_details.payment_method,
            'card_last_four': payment_details.card_last_four,
        })

    return JsonResponse({'success': False})


@login_required
def edit_privacy_settings(request):
    if request.method == 'POST':
        privacy_settings, created = PrivacySettings.objects.get_or_create(
            user=request.user)
        privacy_settings.data_sharing_enabled = (
            'data_sharing_enabled' in request.POST
        )
        privacy_settings.save()

        messages.success(request, 'Privacy settings updated successfully.')
        return redirect('account_settings')
