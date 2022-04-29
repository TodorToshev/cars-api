from django.contrib.auth import get_user_model
from rest_framework import serializers
from cars.models import CarBrand, CarModel, UserCar

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ('password', 'deleted_at', 'groups','user_permissions', )


class CarBrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarBrand
        exclude = ('deleted_at',)


class CarModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarModel
        exclude = ('deleted_at',)


class UserCarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserCar
        exclude = ('deleted_at',)
        