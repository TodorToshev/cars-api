from django.db import models
from accounts.models import CustomUser

from common.soft_delete import SoftDeleteModel
#TODO: soft delete

class CarBrand(SoftDeleteModel):
    name = models.CharField(max_length=120, unique=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # deleted_at = models.DateTimeField(auto_now=True)    #soft_delete. change later.

    def __str__(self):
        return self.name


class CarModel(SoftDeleteModel):
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class UserCar(SoftDeleteModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    first_reg = models.DateField(null=True)
    odometer = models.PositiveIntegerField(default=0)
    # created_at = models.DateTimeField(auto_now_add=True)
    # deleted_at = models.DateTimeField(auto_now=True)    #soft_delete. change later.

    def __str__(self):
        return f"{self.user} - {self.car_brand} {self.car_model}"