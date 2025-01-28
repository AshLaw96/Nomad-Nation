from django.db import models
from django.contrib.auth.models import User


class Amenity(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='amenities', null=False, blank=False, default=1
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

    def __str__(self):
        return self.title


