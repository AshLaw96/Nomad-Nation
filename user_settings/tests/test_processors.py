from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware
from user_settings.models import UserProfile
from user_settings.context_processors import currency_context


class CurrencyContextProcessorTest(TestCase):
    def setUp(self):
        """
        Set up the test environment for the CurrencyContextProcessor tests.
        Initializes a request factory, a user, and a corresponding user profile
        with a currency setting. This method is called before each test case
        to ensure the necessary objects are available for testing.
        """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="testuser", password="password"
        )
        self.profile = UserProfile.objects.create(
            user=self.user, currency="USD"
        )

    def _add_session_to_request(self, request):
        """
        Manually attach a session to the request.
        This helper function simulates session processing in middleware and
        ensures the session is saved and available for use in the request.
        """
        middleware = SessionMiddleware(lambda request: request)
        middleware.process_request(request)
        request.session.save()

    def test_currency_context_authenticated_user(self):
        """
        Test the currency context for an authenticated user with a set
        currency.
        This test ensures that when an authenticated user has a currency set
        in their profile, the `currency_context` function returns the correct
        currency in the context and session.
        """
        request = self.factory.get("/")
        request.user = self.user
        self._add_session_to_request(request)

        context = currency_context(request)
        self.assertEqual(context["user_currency"], "USD")
        self.assertEqual(request.session["currency"], "USD")

    def test_currency_context_anonymous_user(self):
        """
        Test the currency context for an anonymous user (not logged in).
        This test ensures that when an anonymous user makes a request, the
        `currency_context` function defaults to GBP as the currency in both
        the context and session.
        """
        request = self.factory.get("/")
        # Mocking anonymous user
        request.user = type("AnonymousUser", (), {"is_authenticated": False})()
        self._add_session_to_request(request)

        context = currency_context(request)
        self.assertEqual(context["user_currency"], "GBP")
        self.assertEqual(request.session["currency"], "GBP")
