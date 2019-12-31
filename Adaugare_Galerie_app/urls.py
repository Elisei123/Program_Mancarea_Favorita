from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add-eat/', views.add_eat, name = 'add_eat'),
    path('gallery-public/', views.gallery_public, name = 'gallery_public'),
    path('gallery-private/', views.gallery_private, name='gallery_private'),
]