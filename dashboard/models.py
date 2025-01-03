from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    USER_TYPES = [
        ('customer', 'Customer'),
        ('owner', 'Caravan Owner'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    # Explicitly sets related_name to avoid clashes
    groups = models.ManyToManyField(
        Group,
        # Avoids conflict with auth.User.groups
        related_name="customuser_set",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",
        blank=True,
    )

    def __str__(self):
        return self.username
