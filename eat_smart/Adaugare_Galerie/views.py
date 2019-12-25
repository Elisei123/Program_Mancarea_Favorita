# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Mancare
from django.contrib.auth import logout
from time import gmtime, strftime

# Create your views here.


def home(request):
    return render(request, 'home.html')


@login_required
def add_eat(request):
    if request.method == "POST":
        titlul = request.POST['nume']
        descriere = "None"
        imagine = request.FILES['imagine']
        data_publicarii = strftime("%H:%M:%S %d-%m-%Y", gmtime())
        mancare = Mancare(titlul=titlul, descriere=descriere, upload=imagine, username_autor=request.user.username,
                          data_publicarii=data_publicarii)
        mancare.save()
        return redirect('gallery_private')
    else:
        return render(request, 'add-eat.html')

def gallery_public(request):
    exista_un_fel_de_mancare = True
    feluri_mancare = Mancare.objects.all()
    if Mancare.objects.filter().exists():
        return render(request, 'gallery_public.html', {'feluri_mancare':feluri_mancare, 'exista_un_fel_de_mancare': exista_un_fel_de_mancare})
    else:
        exista_un_fel_de_mancare = False
        return render(request, 'gallery_public.html', {'feluri_mancare':feluri_mancare, 'exista_un_fel_de_mancare': exista_un_fel_de_mancare})


def gallery_private(request):
    exista_un_fel_de_mancare = True
    username=request.user
    feluri_mancare = Mancare.objects.filter(username_autor=username)
    if Mancare.objects.filter().exists():
        return render(request, 'gallery_private.html', {'feluri_mancare':feluri_mancare, 'exista_un_fel_de_mancare':exista_un_fel_de_mancare})
    else:
        exista_un_fel_de_mancare = False
        return render(request, 'gallery_private.html', {'feluri_mancare':feluri_mancare, 'exista_un_fel_de_mancare':exista_un_fel_de_mancare})


