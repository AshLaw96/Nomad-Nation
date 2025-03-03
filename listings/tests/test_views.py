from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date, timedelta
from listings.models import Caravan, Booking, Availability
from dashboard.models import UserProfile as DashboardUserProfile
from user_settings.models import UserProfile as SettingsUserProfile


class ListingsViewsTestCase(TestCase):

    def setUp(self):
        # Create Users
        self.owner = User.objects.create_user(
            username="owner", password="password"
        )
        self.customer = User.objects.create_user(
            username="customer", password="password"
        )

        # Create Dashboard UserProfiles (for user type)
        self.owner_profile, _ = DashboardUserProfile.objects.get_or_create(
            user=self.owner
        )
        self.customer_profile, _ = DashboardUserProfile.objects.get_or_create(
            user=self.customer
        )

        # Create User Settings Profiles (for preferences)
        self.owner_settings, _ = SettingsUserProfile.objects.get_or_create(
            user=self.owner
        )
        self.customer_settings, _ = SettingsUserProfile.objects.get_or_create(
            user=self.customer
        )

        # Set user types
        self.owner_profile.user_type = "owner"
        self.customer_profile.user_type = "customer"
        self.owner_profile.save()
        self.customer_profile.save()

        # Ensure UserProfile objects are properly linked
        self.owner.refresh_from_db()
        self.customer.refresh_from_db()

        # Create a Caravan
        self.caravan = Caravan.objects.create(
            owner=self.owner,
            title="Luxury Caravan",
            price_per_night=100.00,
            location="Beachside"
        )

    def test_listings_view(self):
        """Test that listings are displayed correctly."""
        self.client.login(username='customer', password='password')
        response = self.client.get(reverse('listings'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Luxury Caravan")

    def test_add_caravan(self):
        """Test that a caravan is added successfully."""
        self.client.login(username='owner', password='password')
        response = self.client.post(reverse('add_caravan'), {
            'title': 'New Caravan',
            'price_per_night': 120.00,
            'location': 'Mountain View',
            'description': 'Spacious and comfortable',
            'berth': 'medium',
            'available_dates': '[{"start_date": "2025-06-01", "end_date": '
                               '"2025-06-10"}]'
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Caravan.objects.filter(title='New Caravan').exists())

    def test_book_caravan(self):
        """Test that a customer can request a booking."""
        self.client.login(username='customer', password='password')

        # Ensure caravan is available for booking
        Availability.objects.create(
            caravan=self.caravan,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=10)
        )

        response = self.client.post(
            reverse('book_caravan', args=[self.caravan.id]), {
                'start_date': date.today().isoformat(),
                'end_date': (date.today() + timedelta(days=1)).isoformat(),
                'name': 'John Doe',
                'email': 'jD@example.com'
            }, follow=True
        )

        if response.context and 'form' in response.context:
            print(response.context['form'].errors)
        else:
            print("No form errors or context is missing.")

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Booking.objects.filter(
                caravan=self.caravan, customer=self.customer
            ).exists()
        )
