from rest_framework import viewsets
from rest_framework import permissions
from .serializers import (UserSerializer, CarBrandSerializer, 
    CarModelSerializer, UserCarSerializer)
from accounts.models import CustomUser
from cars.models import CarBrand, CarModel, UserCar


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CarBrandViewSet(viewsets.ModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class UserCarViewSet(viewsets.ModelViewSet):
    queryset = UserCar.objects.all()
    serializer_class = UserCarSerializer
