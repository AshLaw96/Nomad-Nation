from .models import UserProfile


def user_currency(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.filter(user=request.user).first()
        if user_profile:
            return {'user_currency': user_profile.currency}
    return {}
