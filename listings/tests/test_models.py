from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date, timedelta
from django.core.exceptions import ValidationError
from listings.models import (
    Amenity, Caravan, Availability, Booking, Review, Reply
)
from dashboard.models import UserProfile


class ModelsTestCase(TestCase):

    def setUp(self):
        """
        Set up test data
        """
        # Create test users
        self.owner = User.objects.create_user(
            username='owner', password='password'
        )
        self.customer = User.objects.create_user(
            username='customer', password='password'
        )
        # Create UserProfile for both users
        self.owner_profile = UserProfile.objects.create(
            user=self.owner, user_type="owner"
        )
        self.customer_profile = UserProfile.objects.create(
            user=self.customer, user_type="customer"
        )

        # Create an amenity
        self.amenity = Amenity.objects.create(name="WiFi", owner=self.owner)
        # Create a caravan
        self.caravan = Caravan.objects.create(
            owner=self.owner,
            title="Luxury Caravan",
            description="A beautiful caravan by the sea",
            berth='medium',
            price_per_night=100.00,
            location="Beachside"
        )
        self.caravan.amenities.add(self.amenity)

    def test_amenity_str(self):
        """
        Test Amenity __str__ method
        """
        self.assertEqual(str(self.amenity), "WiFi")

    def test_caravan_favourites(self):
        """
        Test is_favourite method
        """
        self.assertFalse(self.caravan.is_favourite(self.customer))
        self.caravan.favourites.add(self.customer)
        self.assertTrue(self.caravan.is_favourite(self.customer))

    def test_caravan_availability(self):
        """
        Test is_available property
        """
        future_start = date.today() + timedelta(days=5)
        future_end = future_start + timedelta(days=3)

        # Caravan has no availability initially
        self.assertFalse(self.caravan.is_available)

        # Adding a future availability
        Availability.objects.create(
            caravan=self.caravan,
            start_date=future_start,
            end_date=future_end,
            is_available=True
        )
        self.assertTrue(self.caravan.is_available)

    def test_availability_clean_valid_dates(self):
        """
        Test Availability model allows valid dates
        """
        availability = Availability(
            caravan=self.caravan,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=5),
            is_available=True
        )
        try:
            # Should not raise error
            availability.clean()
        except ValidationError:
            self.fail(
                "Availability clean() raised ValidationError unexpectedly!"
            )

    def test_availability_clean_invalid_dates(self):
        """
        Test Availability model rejects invalid date ranges
        """
        availability = Availability(
            caravan=self.caravan,
            start_date=date.today() + timedelta(days=5),
            end_date=date.today(),
            is_available=True
        )
        with self.assertRaises(ValidationError):
            availability.clean()

    def test_booking_creation(self):
        """
        Test Booking model creation
        """
        booking = Booking.objects.create(
            caravan=self.caravan,
            customer=self.customer,
            name="John Doe",
            email="john@example.com",
            start_date=date.today(),
            end_date=date.today() + timedelta(days=3),
            message="Looking forward to it!"
        )
        expected_str = (
            f"Booking for {self.caravan.title} by {self.customer.username}"
        )
        self.assertEqual(str(booking), expected_str)

    def test_review_creation(self):
        """
        Test Review model __str__ method
        """
        review = Review.objects.create(
            caravan=self.caravan,
            customer=self.customer,
            rating=5,
            comment="Amazing stay!"
        )
        self.assertEqual(
            str(review),
            f"Review for {self.caravan.title} by {self.customer.username}"
        )

    def test_reply_creation(self):
        """
        Test Reply model __str__ method
        """
        review = Review.objects.create(
            caravan=self.caravan,
            customer=self.customer,
            rating=5,
            comment="Amazing stay!"
        )
        reply = Reply.objects.create(
            review=review,
            owner=self.owner,
            reply="Thank you for your feedback!"
        )
        self.assertEqual(
            str(reply),
            f"Reply by {self.owner.username} to review {review.pk}"
        )
