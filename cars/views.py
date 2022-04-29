from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CarBrand, CarModel, UserCar


def list_all(request):
    brands = CarBrand.objects.all()
    models = CarModel.objects.all()
    user_cars = UserCar.objects.all()
    return render(request, 'cars/list.html', {'brands': brands, 'models': models, 'user_cars': user_cars})


class CarBrandCreateView(CreateView):
    model = CarBrand
    fields = ('name',)
    template_name = 'cars/create.html'
    success_url = reverse_lazy('cars:all')


class CarBrandUpdateView(UpdateView):
    model = CarBrand
    fields = ('name',)
    template_name = 'cars/create.html'
    success_url = reverse_lazy('cars:all')


class CarBrandDeleteView(DeleteView):
    model = CarBrand
    template_name = 'cars/delete.html'
    success_url = reverse_lazy('cars:all')


class CarModelCreateView(CreateView):
    model = CarModel
    fields = ('car_brand', 'name',)
    template_name = 'cars/create.html'
    success_url = reverse_lazy('cars:all')


class CarModelUpdateView(UpdateView):
    model = CarModel
    fields = ('car_brand', 'name',)
    template_name = 'cars/create.html'
    success_url = reverse_lazy('cars:all')


class CarModelDeleteView(DeleteView):
    model = CarModel
    template_name = 'cars/delete.html'
    success_url = reverse_lazy('cars:all')


class UserCarCreateView(CreateView):
    model = UserCar
    fields = ('user', 'car_brand', 'car_model', 'first_reg', 'odometer',)
    template_name = 'cars/create.html'
    success_url = reverse_lazy('cars:all')


class UserCarUpdateView(UpdateView):
    model = UserCar
    fields = ('user', 'car_brand', 'car_model', 'first_reg', 'odometer',)
    template_name = 'cars/create.html'
    success_url = reverse_lazy('cars:all')


class UserCarDeleteView(DeleteView):
    model = UserCar
    template_name = 'cars/delete.html'
    success_url = reverse_lazy('cars:all')
