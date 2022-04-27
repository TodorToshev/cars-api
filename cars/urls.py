from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path("all/", views.list_all, name="all"),
    path("brand-create/", views.CarBrandCreateView.as_view(), name="brand_create"),
    path("brand/<int:pk>/update/",
         views.CarBrandUpdateView.as_view(), name='brand_update'),
    path("brand/<int:pk>/delete/",
         views.CarBrandDeleteView.as_view(), name='brand_delete'),
    path("model-create/", views.CarModelCreateView.as_view(), name="model_create"),
    path("model/<int:pk>/update/",
         views.CarModelUpdateView.as_view(), name='model_update'),
    path("model/<int:pk>/delete/",
         views.CarModelDeleteView.as_view(), name='model_delete'),
    path("user-car-create/", views.UserCarCreateView.as_view(),
         name="user_car_create"),
    path("user-car/<int:pk>/update/",
         views.UserCarUpdateView.as_view(), name='user_car_update'),
    path("user-car/<int:pk>/delete/",
         views.UserCarDeleteView.as_view(), name='user_car_delete'),
]
