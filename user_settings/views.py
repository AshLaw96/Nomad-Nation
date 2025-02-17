from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
        # Activate the selected language
        translation.activate(user_profile.language)
        request.session[settings.LANGUAGE_COOKIE_NAME] = user_profile.language

        # Redirect with the language code
        response = HttpResponseRedirect('/user_settings/account_settings/')
        response.set_cookie(
            settings.LANGUAGE_COOKIE_NAME, user_profile.language
        )
        return response
