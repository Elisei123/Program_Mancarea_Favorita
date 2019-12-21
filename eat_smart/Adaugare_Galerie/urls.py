from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add-eat/', views.add_eat, name = 'add_eat'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('adauga_mancare/', views.adauga_mancare, name= 'adauga_mancare'),
]