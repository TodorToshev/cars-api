from rest_framework import viewsets
from django_filters import rest_framework as filters
from .serializers import (UserSerializer, CarBrandSerializer,
                          CarModelSerializer, UserCarSerializer)
from accounts.models import CustomUser
from cars.models import CarBrand, CarModel, UserCar


class UserViewSet(viewsets.ModelViewSet):
    SAFE_METHODS = ['get', 'head', 'options']

    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    http_method_names = SAFE_METHODS


class CarBrandFilter(filters.FilterSet):

    class Meta:
        model = CarBrand
        fields = {
            'name': ['icontains'],
            'created_at': ['iexact', 'lte', 'gte'],
            # 'deleted_at': ['iexact', 'lte', 'gte'],
        }


class CarModelFilter(filters.FilterSet):

    class Meta:
        model = CarModel
        fields = {
            'car_brand': ['exact'],
            'name': ['icontains'],
            'created_at': ['iexact', 'lte', 'gte'],
            'update_at': ['iexact', 'lte', 'gte'],
        }


class UserCarFilter(filters.FilterSet):

    class Meta:
        model = UserCar
        fields = {
            'user': ['exact'],
            'car_brand': ['exact'],
            'car_model': ['exact'],
            'first_reg': ['iexact', 'lte', 'gte'],
            'odometer': ['iexact', 'lte', 'gte'],
            'created_at': ['iexact', 'lte', 'gte'],
            # 'deleted_at': ['iexact', 'lte', 'gte'],
        }


class CarBrandViewSet(viewsets.ModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    filterset_class = CarBrandFilter


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    filterset_class = CarModelFilter


class UserCarViewSet(viewsets.ModelViewSet):
    queryset = UserCar.objects.all()
    serializer_class = UserCarSerializer
    filterset_class = UserCarFilter
    
