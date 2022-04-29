from django.db import models
from django.contrib.auth.models import AbstractUser
from common.soft_delete import SoftDeleteModel


class CustomUser(AbstractUser, SoftDeleteModel):
    date_of_birth = models.DateField(null=True)
    has_drivers_license = models.BooleanField(default=True)
    acquired_license_date = models.DateField(null=True)
    has_traffic_ticket = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
  