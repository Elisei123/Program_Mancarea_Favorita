# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Mancare, Favorit

# Register your models here.

class MancareAdmin(admin.ModelAdmin):
    list_display = ('id', 'username_autor', 'titlul', 'descriere', 'upload', 'data_publicarii')

class FavoritAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_user', 'id_mancare', 'salvat')

admin.site.register(Mancare, MancareAdmin)
admin.site.register(Favorit, FavoritAdmin)