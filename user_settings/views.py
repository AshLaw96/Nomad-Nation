from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.utils import translation
from django.http import HttpResponseRedirect
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

        # Redirect with the language code
        response = HttpResponseRedirect('/user_settings/account_settings/')
        response.set_cookie(
            settings.LANGUAGE_COOKIE_NAME, user_profile.language
        )
        return response


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
