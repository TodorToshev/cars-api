from django.contrib.auth import get_user_model
from rest_framework import serializers
from cars.models import CarBrand, CarModel, UserCar

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ('user_permissions', 'password', 'is_staff', 'groups',)


class CarBrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class UserCarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserCar
        fields = '__all__'
        