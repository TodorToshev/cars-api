from rest_framework import viewsets
from rest_framework import permissions
from django_filters import rest_framework as filters
from .serializers import (UserSerializer, CarBrandSerializer, 
    CarModelSerializer, UserCarSerializer)
from accounts.models import CustomUser
from cars.models import CarBrand, CarModel, UserCar


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    

class CarBrandViewSet(viewsets.ModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = '__all__'
    # filterset_fields = ('name', 'created_at', 'deleted_at')


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = '__all__'


class UserCarViewSet(viewsets.ModelViewSet):
    queryset = UserCar.objects.all()
    serializer_class = UserCarSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = '__all__'
