# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Mancare, Favorit
from django.contrib.auth import logout
from time import gmtime, strftime
from django.contrib import messages


# Create your views here.

def error_404_view(request, exception):
    return render(request,'error_404.html')

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
    feluri_mancare = Mancare.objects.all().order_by('-id')
    username_curent = request.user.username
    mancaruri_favorite = Favorit.objects.filter(id_user=request.user.id).order_by('-id')
    id_uri_mancaruri_favorite = []
    for mancare_favorita in mancaruri_favorite:
        id_uri_mancaruri_favorite.append(mancare_favorita.id_mancare)

    if Mancare.objects.filter().exists():
        return render(request, 'gallery_public.html',
                  {'feluri_mancare':feluri_mancare,
                   'exista_un_fel_de_mancare': exista_un_fel_de_mancare,
                   'username_curent': username_curent,
                   'id_uri_mancaruri_favorite':id_uri_mancaruri_favorite})
    else:
        exista_un_fel_de_mancare = False
        return render(request, 'gallery_public.html',
                  {'feluri_mancare':feluri_mancare,
                   'exista_un_fel_de_mancare': exista_un_fel_de_mancare,
                   'username_curent': username_curent})


def gallery_private(request):
    exista_un_fel_de_mancare = True
    username=request.user
    feluri_mancare = Mancare.objects.filter(username_autor=username).order_by('-id')
    if Mancare.objects.filter().exists():
        return render(request,
              'gallery_private.html',
              {'feluri_mancare':feluri_mancare,
               'exista_un_fel_de_mancare':exista_un_fel_de_mancare})
    else:
        exista_un_fel_de_mancare = False
        return render(request,
              'gallery_private.html',
              {'feluri_mancare':feluri_mancare,
               'exista_un_fel_de_mancare':exista_un_fel_de_mancare})

def favorit(request):
    id_user = request.user.id
    favorite = Favorit.objects.filter(id_user=id_user).order_by('-id')

    id_uri_mancaruri_favorite = []
    for fav in favorite:
        id_uri_mancaruri_favorite.append(fav.id_mancare)

    mancaruri_favorite = Mancare.objects.filter(id__in=id_uri_mancaruri_favorite)

    return render(
        request,
        "favorit.html",
        {'mancaruri_favorite': mancaruri_favorite})

def salvare(request, fel_de_mancare_id):
    #TODO: Verifica daca id-ul se afla deja in baza de date. (id-ul mancarii, pentru a prevenii spam-ul.

    Mancare_object=Mancare.objects.get(pk=fel_de_mancare_id)
    user_curent = request.user
    id_user=user_curent.id
    id_mancare=Mancare_object.id
    if Favorit.objects.filter(id_mancare=id_mancare).exists():
        messages.info(request, "Aceasta mancare a fost deja adaugata la favorit!")
        return render(request,'error_404.html')
    else:
        favorit_object = Favorit(id_user=id_user, id_mancare=id_mancare, salvat=True)
        print("Done save on FAVORIT")
        favorit_object.save()
        messages.info(request, "Mancarea a fost salvata cu succes la 'Favorit'")
        return redirect('/gallery-public/')


    # TODO: Fa atunci cand dai click pe butonul salveaza sa te duca direct la href-ul unde ai apsat pe buton (ex: fel_de_mancare_id)
    # TODO:p.s: vezi daca ii poti baga animatie.