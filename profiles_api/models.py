from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    #User Profile Manager
    def create_user(self,email,name,password=None):
        # Create New User Profile
        if not email:
            raise ValueError("Please enter an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        # Save User Data
        user.save(using=self.db)

        return user
    
    #Create SuperUser

    def create_superuser(self, email,name, password):
        user =self.create_superuser(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

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
