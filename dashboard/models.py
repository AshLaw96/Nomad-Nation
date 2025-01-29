from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    USER_TYPES = [
        ('customer', 'Customer'),
        ('owner', 'Caravan Owner'),
    ]
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    user_type = models.CharField(
        max_length=8,
        choices=USER_TYPES,
        default='customer'
    )

    def __str__(self):
        return f"{self.user.username} ({self.user_type})"
