from django.utils import translation
from django.conf import settings
from .models import UserProfile


class UserLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                language = user_profile.language
            except UserProfile.DoesNotExist:
                language = settings.LANGUAGE_CODE
        else:
            language = settings.LANGUAGE_CODE

        translation.activate(language)
        request.session[settings.LANGUAGE_COOKIE_NAME] = language
        response = self.get_response(request)
        translation.deactivate()
        return response
