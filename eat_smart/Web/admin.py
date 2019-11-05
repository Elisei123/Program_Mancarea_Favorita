# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Mancare

# Register your models here.

class MancareAdmin(admin.ModelAdmin):
    list_display = ('titlul', 'descriere', 'upload')

admin.site.register(Mancare, MancareAdmin)