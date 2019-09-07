from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.home),
    path('register/', views.home),
]