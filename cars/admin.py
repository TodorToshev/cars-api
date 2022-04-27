from django.contrib import admin
from .models import CarBrand, CarModel, UserCar

admin.site.register(CarBrand)
admin.site.register(CarModel)
admin.site.register(UserCar)
