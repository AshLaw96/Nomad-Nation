from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.utils import translation
from django.http import JsonResponse
import json
from .models import UserProfile, PaymentDetails, PrivacySettings
from .currency import convert_currency


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
    if request.method == 'POST':
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.language = request.POST['language']
        user_profile.currency = request.POST['currency']
        user_profile.appearance = request.POST['appearance']
        user_profile.notifications = 'notifications' in request.POST
        user_profile.save()

        # Activate the selected language
        translation.activate(user_profile.language)
        request.session[settings.LANGUAGE_COOKIE_NAME] = user_profile.language

        # Return JSON response
        return JsonResponse({
            'currency': user_profile.currency,
            'message': 'Preferences updated successfully.'
        })


def convert_price_view(request):
    amount = float(request.GET.get('amount', 0))
    from_currency = request.GET.get('from', 'GBP')
    to_currency = request.GET.get('to', 'GBP')

    # Convert only if necessary
    if from_currency != to_currency:
        converted_price = convert_currency(amount, from_currency, to_currency)
    else:
        converted_price = amount

    return JsonResponse({'converted_price': converted_price})


@login_required
def edit_payment_details(request):
    if request.method == 'POST':
        payment_details, created = PaymentDetails.objects.get_or_create(
            user=request.user)
        payment_details.payment_method = request.POST['payment_method']
        payment_details.card_last_four = request.POST['card_last_four']
        payment_details.billing_address = request.POST['billing_address']
        payment_details.save()

        messages.success(request, 'Payment details updated successfully.')
        return redirect('account_settings')


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


@login_required
def convert_currency_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_currency = data['new_currency']
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile.currency = new_currency
            user_profile.save()

            # Get the conversion rate
            rate = convert_currency(1, 'GBP', new_currency)

            return JsonResponse({'rate': rate})

        except KeyError as e:
            messages.error(request, f"Error: {str(e)}")
            return JsonResponse({'error': str(e)}, status=400)

        except Exception:
            messages.error(request, 'An unexpected error occurred.')
            return JsonResponse(
                {'error': 'An unexpected error occurred.'}, status=500
            )
