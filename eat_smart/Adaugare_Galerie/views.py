# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .models import Mancare
from django.contrib.auth import logout

# Create your views here.


def home(request):
    return render(request, 'home.html')

def add_eat(request):
    if request.method == "POST":
        titlul = request.POST['nume']
        descriere = "None"
        imagine = request.FILES['imagine']
        username=request.user
        print(username.username)
        mancare = Mancare(titlul=titlul, descriere=descriere, upload=imagine, username_autor=username)
        mancare.save()
        return redirect('gallery')
    else:
        return render(request, 'add-eat.html')



def gallery_public(request):
    feluri_mancare = Mancare.objects.all()
    return render(request, 'gallery_public.html', {'feluri_mancare':feluri_mancare})

def gallery_private(request):
    username=request.user
    feluri_mancare = Mancare.objects.filter(username_autor=username)
    return render(request, 'gallery_private.html', {'feluri_mancare':feluri_mancare})

