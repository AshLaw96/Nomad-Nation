from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date


class Amenity(models.Model):
    """
    Represents an amenity that can be associated with a caravan.
    Each amenity is owned by a user.
    """
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='amenities',
        null=False,
        blank=False,
        default=1
    )

    def __str__(self):
        return self.name


class Caravan(models.Model):
    """
    Represents a caravan listing with details such as title, description,
    berth capacity, price, location, and associated amenities.
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='caravans'
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    berth = models.CharField(
        max_length=10, choices=[
            ('small', _('Two-berth')),
            ('medium', _('Four-berth')),
            ('large', _('Six-berth'))
        ]
    )
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(max_length=3, default="GBP")
    location = models.CharField(max_length=100)
    amenities = models.ManyToManyField(Amenity, related_name='caravans')
    favourites = models.ManyToManyField(
        User, related_name='favourite_caravans', blank=True
    )

    def is_favourite(self, user):
        """
        Checks if the given user has favourited this caravan.
        """
        return self.favourites.filter(id=user.id).exists()

    @property
    def is_available(self):
        """
        Checks if the caravan has future availability.
        """
        today = date.today()
        future_availabilities = self.availabilities.filter(
            start_date__gt=today, is_available=True
        )
        return future_availabilities.exists()


class CaravanImage(models.Model):
    """
    Represents an image associated with a specific caravan.
    """
    caravan = models.ForeignKey(
        Caravan, on_delete=models.CASCADE, related_name='images'
    )
    image = models.ImageField(upload_to='static/images/')

    def __str__(self):
        return _("Image for") + f" {self.caravan.title}"


class Availability(models.Model):
    """
    Represents the availability periods for a caravan.
    """
    caravan = models.ForeignKey(
        Caravan, on_delete=models.CASCADE,
        related_name='availabilities'
    )
    start_date = models.DateField(blank=False)
    end_date = models.DateField(null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        """
        Returns a string representation of the availability period.
        """
        return (
            f"{self.caravan.title if self.caravan else 'No Caravan'}: "
            f"{self.start_date} to "
            f"{self.end_date}"
        )

    def clean(self):
        """
        Validates that the start date is before the end date.
        """
        if (
            self.start_date and self.end_date and
            self.start_date > self.end_date
        ):
            raise ValidationError(_("End date must be after start date."))


class Booking(models.Model):
    """
    Represents a booking request for a caravan.
    Includes customer details and booking status.
    """
    STATUS_CHOICES = [
        ("pending", _("Pending")),
        ("accepted", _("Accepted")),
        ("declined", _("Declined")),
    ]

    caravan = models.ForeignKey(
        Caravan, on_delete=models.CASCADE, related_name="bookings"
    )
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings"
    )
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    message = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="pending"
    )

    def __str__(self):
        """
        Returns a string representation of the booking.
        """
        return (
            _("Booking for") + f" {self.caravan.title}" +
            _(" by ") + f"{self.customer.username}"
        )


class Review(models.Model):
    """
    Represents a customer review for a caravan.
    Includes a rating, comment, and approval status.
    """
    caravan = models.ForeignKey(
        Caravan, on_delete=models.CASCADE, related_name='reviews'
    )
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation of the review.
        """
        return (
            _("Review for") + f" {self.caravan.title} " +
            _("by") + f" {self.customer.username}"
        )


class Reply(models.Model):
    """
    Represents a reply to a review, typically from a caravan owner.
    """
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='replies'
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='replies'
    )
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the reply.
        """
        return (
            _("Reply by") + f" {self.owner.username} " +
            _("to review") + f" {self.review.pk}"
        )
