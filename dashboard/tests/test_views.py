from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from dashboard.models import UserProfile
from listings.models import Caravan, Booking, Review
from django.utils import timezone

User = get_user_model()


class DashboardViewTests(TestCase):
    """
    Tests for the dashboard_view
    """

    def setUp(self):
        """
        Set up test users, profiles, and sample data
        """
        self.customer = User.objects.create_user(
            username="customer", password="testpass"
        )
        self.owner = User.objects.create_user(
            username="owner", password="testpass"
        )
        self.superuser = User.objects.create_superuser(
            username="admin", password="adminpass"
        )

        # Create profiles
        self.customer_profile = UserProfile.objects.create(
            user=self.customer, user_type="customer"
        )
        self.owner_profile = UserProfile.objects.create(
            user=self.owner, user_type="owner"
        )

        # Create sample data
        self.caravan = Caravan.objects.create(
            owner=self.owner,
            title="Luxury Caravan",
            location="Blackpool",
            price_per_night=100.00
        )
        self.booking = Booking.objects.create(
            customer=self.customer,
            caravan=self.caravan,
            status="accepted",
            start_date=timezone.now() + timezone.timedelta(days=5),
            end_date=timezone.now() + timezone.timedelta(days=10)
        )
        self.review = Review.objects.create(
            caravan=self.caravan,
            customer=self.customer,
            approved=True,
            rating=5,
            comment="Great caravan!"
        )

    def test_dashboard_requires_login(self):
        """
        Test that the dashboard redirects unauthenticated users
        """
        response = self.client.get(reverse("dashboard"))
        expected_url = f"/accounts/login/?next={reverse('dashboard')}"
        self.assertRedirects(response, expected_url)

    def test_superuser_dashboard(self):
        """Test that a superuser sees the correct dashboard"""
        self.client.login(username="admin", password="adminpass")
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/dashboard.html")
        self.assertEqual(response.context["user_type"], "superuser")
        self.assertIn("admin_url", response.context)

    def test_customer_dashboard(self):
        """
        Test that a customer sees the correct dashboard with upcoming stays
        """
        self.client.login(username="customer", password="testpass")
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/dashboard.html")
        self.assertEqual(response.context["user_type"], "customer")
        self.assertIn(self.booking, response.context["upcoming_stays"])

    def test_owner_dashboard(self):
        """
        Test that an owner sees the correct dashboard with caravan listings
        """
        self.client.login(username="owner", password="testpass")
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/dashboard.html")
        self.assertEqual(response.context["user_type"], "owner")
        self.assertIn(self.caravan, response.context["caravans"])
        self.assertIn(self.review, response.context["reviews"])

    def test_redirect_if_no_profile(self):
        """Test that users without a profile are logged out"""
        User.objects.create_user(username="noprof", password="testpass")
        self.client.login(username="noprof", password="testpass")
        response = self.client.get(reverse("dashboard"))
        self.assertRedirects(response, reverse("account_logout"))
