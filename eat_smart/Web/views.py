# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

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

def adaugare_mancare(request):
    if request.method == 'POST':
        nume = request.POST['nume']
        descriere = request.POST['descriere']
        imagine = request.POST['imagine']
        return render('/')
    else:
        return render(request, '/add-eat')
