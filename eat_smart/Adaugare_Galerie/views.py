# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.shortcuts import render
from .models import Mancare
from django.contrib.auth import logout

# Create your views here.


def home(request):
    return render(request, 'home.html')

def add_eat(request):
    if request.method == "POST":
        titlul = request.POST['nume']
        descriere = request.POST['descriere']
        imagine = request.FILES['imagine']
        mancare = Mancare(titlul=titlul, descriere=descriere, upload=imagine)
        mancare.save()
    return render(request, 'add-eat.html')

def gallery(request):
    return render(request, 'gallery.html')

