from django.db import models
from django.contrib.auth.models import AbstractUser

#TODO: soft delete


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True)
    has_drivers_license = models.BooleanField(default=True)
    acquired_license_date = models.DateField(null=True)
    has_traffic_ticket = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
  

class CarBrand(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=True)    #soft_delete. change later.

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class UserCar(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    first_reg = models.DateTimeField()        #must not have auto_now/auto_now_add
    odometer = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=True)    #soft_delete. change later.

    def __str__(self):
        return f"{self.user} - {self.car_brand} {self.car_model}"