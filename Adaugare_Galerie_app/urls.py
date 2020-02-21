from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add-eat/', views.add_eat, name = 'add_eat'),
    path('gallery-public/', views.gallery_public, name = 'gallery_public'),
    path('gallery-private/', views.gallery_private, name='gallery_private'),
    path('favorit/', views.favorit, name='favorit'),
    path('salvare/<fel_de_mancare_id>', views.salvare, name='salvare'),
    path('delete/<fel_mancare_id>', views.delete, name='delete'),
    path('add_like/<add_like_meal>', views.add_like, name='add_like'),
]