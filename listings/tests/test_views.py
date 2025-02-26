from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date, timedelta
from listings.models import Caravan, Booking, Review, Availability
from dashboard.models import UserProfile


class ListingsViewsTestCase(TestCase):

    def setUp(self):
        # Create users
        self.owner = User.objects.create_user(
                username='owner',
                password='password'
            )
        self.customer = User.objects.create_user(
            username='customer', password='password'
        )

        # Create user profiles
        self.owner_profile = UserProfile.objects.create(
            user=self.owner, user_type='owner'
        )
        self.customer_profile = UserProfile.objects.create(
            user=self.customer, user_type='customer'
        )

        # Create a caravan
        self.caravan = Caravan.objects.create(
            owner=self.owner,
            title="Luxury Caravan",
            price_per_night=100.00,
            location="Beachside"
        )

    def test_listings_view(self):
        """
        Test that listings are displayed correctly.
        """
        self.client.login(username='customer', password='password')

        # Ensure user profile exists with a user_type
        self.customer.profile.user_type = 'customer'
        self.customer.profile.save()

        response = self.client.get(reverse('listings'))

        # Expecting a 200 response if logged in correctly
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Luxury Caravan")

    def test_add_caravan(self):
        """
        Test that a caravan is added successfully.
        """
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

        # DEBUG: Print response details
        print(f"Response Status Code: {response.status_code}")
        print(f"Response URL: {response.redirect_chain}")

        # DEBUG: Print raw response if context is missing
        if response.context is None:
            print("Response Content:", response.content.decode())

        # Redirect after successful add
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Caravan.objects.filter(title='New Caravan').exists())

    def test_edit_caravan(self):
        """
        Test that an owner can edit their caravan.
        """
        self.client.login(username='owner', password='password')
        response = self.client.post(
            reverse('edit_caravan', args=[self.caravan.id]),
            {
                'title': 'Updated Caravan',
                'price_per_night': 150.00,
                'location': 'Updated Location',
                'description': 'Updated description',
                'berth': 'medium',
                'available_dates': '[{"start_date": "2025-06-01", "end_date": '
                                   '"2025-06-10"}]'
            },
            follow=True
        )

        # DEBUG: Print response details
        print(f"Response Status Code: {response.status_code}")
        print(f"Response URL: {response.redirect_chain}")

        # DEBUG: Print response content if context is missing
        if response.context is None:
            print("Response Content:", response.content.decode())

        # Refresh from the database
        self.caravan.refresh_from_db()
        self.assertEqual(self.caravan.title, 'Updated Caravan')

    def test_delete_caravan(self):
        """
        Test that an owner can delete their caravan.
        """
        self.client.login(username='owner', password='password')
        self.client.post(reverse('delete_caravan', args=[self.caravan.id]))
        self.assertFalse(Caravan.objects.filter(id=self.caravan.id).exists())

    def test_toggle_favourite(self):
        """
        Test that a user can add/remove a caravan from favorites.
        """
        self.client.login(username='customer', password='password')
        response = self.client.post(
            reverse('toggle_favourite', args=[self.caravan.id])
        )
        # Should return JSON response
        self.assertEqual(response.status_code, 200)

    def test_book_caravan(self):
        """
        Test that a customer can request a booking.
        """
        self.client.login(username='customer', password='password')
        # Ensure caravan is available for booking
        Availability.objects.create(
            caravan=self.caravan,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=10)
        )

        response = self.client.post(
            reverse('book_caravan', args=[self.caravan.id]),
            {
                'start_date': date.today().isoformat(),
                'end_date': (date.today() + timedelta(days=1)).isoformat(),
                'name': 'John Doe',
                'email': 'jD@example.com'
            },
            follow=True
        )

        # Print form errors if present
        print(
            response.context.get('form').errors
            if response.context else "No form context"
        )

        # Redirect after booking
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Booking.objects.filter(
                caravan=self.caravan, customer=self.customer
            ).exists()
        )

    def test_manage_booking(self):
        """
        Test that an owner can accept/decline a booking.
        """
        booking = Booking.objects.create(
            caravan=self.caravan,
            customer=self.customer,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=3),
            status='pending'
        )

        self.client.login(username='owner', password='password')
        response = self.client.post(
            reverse('manage_booking', args=[booking.id]),
            {'action': 'accept'},
            follow=True
        )
        # Reload the booking from the database
        booking.refresh_from_db()
        # Redirect expected
        self.assertEqual(response.status_code, 200)
        # Ensure the status was updated
        self.assertEqual(booking.status, 'accepted')

    def test_submit_review(self):
        """
        Test that a customer can submit a review.
        """
        self.client.login(username='customer', password='password')
        response = self.client.post(
            reverse('submit_review', args=[self.caravan.id]),
            {
                'rating': 5,
                'comment': 'Amazing experience!',
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Review.objects.filter(
                caravan=self.caravan, customer=self.customer
            ).exists()
        )
