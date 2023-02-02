from accounts.managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

# --------------
# User Model ---
# --------------


class User(AbstractBaseUser, PermissionsMixin):

    # Define Gender choice
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    phone_number = models.CharField(max_length=400, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.username
