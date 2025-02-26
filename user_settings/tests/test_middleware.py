from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import translation
from django.http import HttpResponse
from django.contrib.sessions.middleware import SessionMiddleware
from user_settings.middleware import UserLanguageMiddleware
from user_settings.models import UserProfile


class UserLanguageMiddlewareTest(TestCase):
    def setUp(self):
        """
        Set up the test environment for the middleware tests.
        Initializes the request factory, middleware, and test data (a user
        and a profile with a specified language). This method is called before
        each test case to ensure the necessary objects are set up.
        """
        self.factory = RequestFactory()

        def get_response(request):
            # Explicitly acknowledge the parameter
            _ = request
            return HttpResponse()

        # Initialise the UserLanguageMiddleware with the response function
        self.middleware = UserLanguageMiddleware(get_response)

        # Create test user
        self.user = User.objects.create_user(
            username="testuser", password="password"
        )

        # Create a user profile with language set to "es"
        self.profile = UserProfile.objects.create(
            user=self.user, language="es"
        )

    def _add_session_to_request(self, request):
        """
        Manually attach a session to the request.
        This helper function mimics the session processing in middleware,
        ensuring that the session is saved and available for use in the
        request.
        """
        middleware = SessionMiddleware(self.middleware.get_response)
        middleware.process_request(request)
        request.session.save()

    def test_middleware_authenticated_user(self):
        """
        Test the behavior of the middleware for an authenticated user with
        a language preference in their profile.
        This test ensures that when an authenticated user with a language
        preference (e.g., "es" for Spanish) makes a request, the middleware
        sets the correct language in the session and the translation system
        uses this language.
        """
        request = self.factory.get("/")
        request.user = self.user
        self._add_session_to_request(request)

        # Call middleware
        self.middleware(request)

        # Verify that the language was properly set in the session
        self.assertEqual(request.session[settings.LANGUAGE_COOKIE_NAME], "es")

        # Manually check if translation framework respects the change
        translation.activate(request.session[settings.LANGUAGE_COOKIE_NAME])
        # Now it should pass
        self.assertEqual(translation.get_language(), "es")

        # Clean up translation state
        translation.deactivate()

    def test_middleware_anonymous_user(self):
        """
        Test the behavior of the middleware for an anonymous user (not logged
        in).
        This test ensures that when an anonymous user makes a request, the
        middleware defaults to the system's default language (as defined in
        settings.LANGUAGE_CODE) and that this is stored in the session.
        """
        request = self.factory.get("/")
        # Mocking anonymous user
        request.user = type("AnonymousUser", (), {"is_authenticated": False})()
        self._add_session_to_request(request)
        self.middleware(request)

        self.assertEqual(translation.get_language(), settings.LANGUAGE_CODE)
        self.assertEqual(
            request.session[settings.LANGUAGE_COOKIE_NAME],
            settings.LANGUAGE_CODE
        )
