from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django_countries.fields import CountryField

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('First name'), max_length=50, blank=True)
    last_name = models.CharField(_('Last name'), max_length=50, blank=True)
    mobile = models.CharField(_('Phone Number'), max_length=20, blank=True, null=True)
    country = CountryField(null=True, blank=True) 
    avatar = models.ImageField(_('Profile image'), upload_to='avatars/', blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def sponsorMedicine(self):
        pass
    
    def sponsorTreatment(self):
        pass

    def cancelSponsorMedicine(self):
        pass

    def cancleSponsorTreatment(self):
        pass