from django.utils import translation
from django.conf import settings
from .models import UserProfile


class UserLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            user_profile = UserProfile.objects.get(user=request.user)
            language = user_profile.language
        else:
            language = settings.LANGUAGE_CODE

        print(f"Activating language: {language}")
        translation.activate(language)
        request.session[settings.LANGUAGE_COOKIE_NAME] = language
        response = self.get_response(request)
        translation.deactivate()
        return response
