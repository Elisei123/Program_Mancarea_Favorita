# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Mancare

# Create your views here.


def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def add_eat(request):
    return render(request, 'add-eat.html')

def gallery(request):
    return render(request, 'gallery.html')

def adauga_mancare(request):
    #Poti sa folosesti GET, dar este mai riscant, deoarece iti poate da flood, spam - link
    titlul = request.POST['nume']
    descriere = request.POST['descriere']
    imagine = request.POST['imagine']
    mancare = Mancare(titlul=titlul, descriere=descriere, upload=imagine)
    mancare.save()
    return render(request, 'add-eat.html')
