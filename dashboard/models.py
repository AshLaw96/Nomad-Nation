from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    Represents additional user information, extending the built-in User model.
    Each user has a profile that specifies their type
    (Customer or Caravan Owner).
    """
    USER_TYPES = [
        ('customer', 'Customer'),
        ('owner', 'Caravan Owner'),
    ]
    user = models.OneToOneField(
        User,
        # Deletes the profile when the user is deleted.
        on_delete=models.CASCADE,
        # Allows accessing the profile from the User model (user.profile).
        related_name='profile'
    )
    user_type = models.CharField(
        # Defines the maximum length of the user type field.
        max_length=8,
        # Restricts choices to "Customer" or "Caravan Owner".
        choices=USER_TYPES,
        # Sets the default user type as "Customer".
        default='customer'
    )

    def __str__(self):
        """
        Returns a string representation of the user profile, displaying
        the username and user type.
        """
        return f"{self.user.username} ({self.user_type})"
