from .models import UserProfile


def currency_context(request):
    """
    Retrieves the preferred currency of the authenticated user and stores it
    in the session.
    - If the user is logged in, their preferred currency is fetched from their
      profile.
    - If no profile exists or the user is not logged in, GBP is used as the
      default currency.
    - The selected currency is stored in the session for easy access
      throughout the application.
    Returns:
        dict: A dictionary containing the user's preferred currency.
    """
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.filter(user=request.user).first()
        currency = user_profile.currency if user_profile else "GBP"
    else:
        # Default currency
        currency = "GBP"

    request.session["currency"] = currency
    return {"user_currency": currency}
