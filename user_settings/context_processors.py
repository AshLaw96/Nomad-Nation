from .models import UserProfile


def currency_context(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.filter(user=request.user).first()
        currency = user_profile.currency if user_profile else "GBP"
    else:
        # Default currency
        currency = "GBP"

    request.session["currency"] = currency
    return {"user_currency": currency}
