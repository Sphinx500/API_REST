from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Create your models here.


class UserProfile(AbstractBaseUser,PermissionsMixin):
    # Models Database Sistem User
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRE_FIELDS = ['name']
    # Get full name
    def get_full_name(self):
        return self.name
    # Get short name
    def get_short_name(self):
        return self.name

    def __str__(self):
        # Return String representation of user
        return self.name
