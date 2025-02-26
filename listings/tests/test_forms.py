from django.test import TestCase
from datetime import date, timedelta
from django.contrib.auth.models import User
from listings.models import Caravan, Amenity, Booking
from listings.forms import CaravanForm, BookingForm, ReviewForm, ReplyForm
import json


class FormsTestCase(TestCase):

    def setUp(self):
        """
        Set up test data
        """
        self.owner = User.objects.create_user(
            username='owner', password='password'
        )
        self.customer = User.objects.create_user(
            username='customer', password='password'
        )

        self.caravan = Caravan.objects.create(
            owner=self.owner,
            title="Luxury Caravan",
            price_per_night=100,
            location="Beachside"
        )

        self.amenity = Amenity.objects.create(name="WiFi", owner=self.owner)

    def test_caravan_form_valid(self):
        """
        Test CaravanForm with valid data
        """
        form = CaravanForm(
            data={
                'title': 'New Caravan',
                'description': 'Spacious and comfortable',
                'berth': 'Four',
                'amenities': [self.amenity.id],
                'location': 'Mountain View',
                'price_per_night': '120.00',
                'available_dates': json.dumps([
                    {"start_date": "2025-06-01", "end_date": "2025-06-10"}
                ])
            },
            user=self.owner
        )
        form.fields["amenities"].queryset = Amenity.objects.filter(
            owner=self.owner
        )

    def test_caravan_form_invalid_dates(self):
        """
        Test CaravanForm with invalid date format
        """
        form = CaravanForm(
            data={
                'title': 'Invalid Dates Caravan',
                'available_dates': "invalid json format"
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('available_dates', form.errors)

    def test_caravan_form_extra_amenity_existing(self):
        """
        Test CaravanForm extra_amenity validation
        """
        Amenity.objects.create(name="Pool", owner=self.owner)
        form = CaravanForm(
            data={
                'title': 'Luxury',
                'extra_amenity': 'Pool'
            },
            instance=self.caravan
        )
        self.assertFalse(form.is_valid())
        self.assertIn('extra_amenity', form.errors)

    def test_booking_form_valid(self):
        """
        Test BookingForm with valid data
        """
        form = BookingForm(
            data={
                'name': 'John Doe',
                'email': 'john@example.com',
                'phone_number': '1234567890',
                'start_date': date.today(),
                'end_date': date.today() + timedelta(days=3),
                'message': 'Looking forward to the stay!'
            },
            caravan=self.caravan
        )
        self.assertTrue(form.is_valid())

    def test_booking_form_invalid_dates(self):
        """
        Test BookingForm when start_date is after end_date
        """
        form = BookingForm(
            data={
                'name': 'John Doe',
                'start_date': date.today() + timedelta(days=3),
                'end_date': date.today()
            },
            caravan=self.caravan
        )
        self.assertFalse(form.is_valid())
        # Clean method raises form-wide error
        self.assertIn('__all__', form.errors)

    def test_booking_form_overlapping_dates(self):
        """
        Test BookingForm rejects overlapping bookings
        """
        Booking.objects.create(
            caravan=self.caravan,
            customer=self.customer,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=5),
            status="accepted"
        )

        form = BookingForm(
            data={
                'name': 'Jane Doe',
                'start_date': date.today() + timedelta(days=2),
                'end_date': date.today() + timedelta(days=6)
            },
            caravan=self.caravan
        )
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)

    def test_review_form_valid(self):
        """
        Test ReviewForm with valid input
        """
        form = ReviewForm(data={'rating': 5, 'comment': 'Great experience!'})
        self.assertTrue(form.is_valid())

    def test_reply_form_valid(self):
        """
        Test ReplyForm with valid input
        """
        form = ReplyForm(data={'reply': 'Thank you!'})
        self.assertTrue(form.is_valid())
