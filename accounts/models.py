from django.db import models
from django.contrib.auth.models import AbstractUser

# From DRF Docs: "..place this code snippet in an installed models.py module, or 
# some other location that will be imported by Django on startup."
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

#probably not needed
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True)
    has_drivers_license = models.BooleanField(default=True)
    acquired_license_date = models.DateField(null=True)
    has_traffic_ticket = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
  