from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date


class Amenity(models.Model):
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
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='caravans'
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    berth = models.CharField(
        max_length=10, choices=[
            ('small', 'Two-berth'),
            ('medium', 'Four-berth'),
            ('large', 'Six-berth')
        ]
    )
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=100)
    amenities = models.ManyToManyField(Amenity, related_name='caravans')
    is_favourite = models.BooleanField(default=False)

    @property
    def is_available(self):
        today = date.today()
        future_availabilities = self.availabilities.filter(
            start_date__gt=today, is_available=True
        )
        return future_availabilities.exists()


class CaravanImage(models.Model):
    caravan = models.ForeignKey(
        Caravan, on_delete=models.CASCADE, related_name='images'
    )
    image = models.ImageField(upload_to='static/images/')

    def __str__(self):
        return f"Image for {self.caravan.title}"


class Availability(models.Model):
    caravan = models.ForeignKey(
        Caravan, on_delete=models.CASCADE,
        related_name='availabilities'
    )
    start_date = models.DateField(blank=False)
    end_date = models.DateField(null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return (
            f"{self.caravan.title if self.caravan else 'No Caravan'}: "
            f"{self.start_date} to "
            f"{self.end_date}"
        )

    def clean(self):
        if (
            self.start_date and self.end_date and
            self.start_date > self.end_date
        ):
            raise ValidationError("End date must be after start date.")


class Booking(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("declined", "Declined"),
    ]

    caravan = models.ForeignKey(
        Caravan, on_delete=models.CASCADE, related_name="bookings"
    )
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings"
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    message = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="pending"
    )

    def __str__(self):
        return f"Booking for {self.caravan.title} by {self.customer.username}"


class Review(models.Model):
    caravan = models.ForeignKey(
        Caravan, on_delete=models.CASCADE, related_name='reviews'
    )
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    reply = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Review for {self.caravan.title} by {self.customer.username}"
