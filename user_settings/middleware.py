from django.utils import translation
from django.conf import settings
from .models import UserProfile


class UserLanguageMiddleware:
    """
    Middleware to set the language preference for authenticated users.

    - If the user is logged in, their preferred language is retrieved from
      their profile.
    - If no profile exists or the user is not logged in, the default language
      from settings is used.
    - The selected language is activated for the current request and stored
      in the session.
    - After processing the request, translation is deactivated to avoid
      affecting other requests.
    This ensures that users experience the application in their preferred
    language.
    """
    def __init__(self, get_response):
        """
        Initialise middleware with the next response handler.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Process the request by setting the appropriate language.
        - Retrieves the language preference from the user's profile.
        - Activates the selected language for the current request.
        - Stores the language in the session for persistence.
        - Deactivates translation after processing the request.
        Returns:
            HttpResponse: The response object after processing the request.
        """
        if request.user.is_authenticated:
            try:
                # Fetch the user's profile to get their preferred language
                user_profile = UserProfile.objects.get(user=request.user)
                language = user_profile.language
            except UserProfile.DoesNotExist:
                # Default to the system language if no profile exists
                language = settings.LANGUAGE_CODE
        else:
            # Use the default system language for unauthenticated users
            language = settings.LANGUAGE_CODE

        translation.activate(language)
        # Store the language preference in the session
        request.session[settings.LANGUAGE_COOKIE_NAME] = language
        response = self.get_response(request)
        # Deactivate translation after the response is generated
        translation.deactivate()
        return response
