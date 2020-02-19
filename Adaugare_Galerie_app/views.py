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
    username_curent = request.user.username

    feluri_mancare = Mancare.objects.all().order_by('-id')
    id_mancaruri_favorite = list(
        Favorit.objects.filter(id_user=request.user.id).values_list('id_mancare', flat=True)
    )

    for fel_mancare in feluri_mancare:
        mancare_favorita = fel_mancare.id in id_mancaruri_favorite
        fel_mancare.este_favorit = mancare_favorita

    return render(
        request,
        'gallery_public.html',
        {
            'feluri_mancare': feluri_mancare,
            'username_curent': username_curent,
        },
    )


# Pagina 'Galerie Privata'
def gallery_private(request):
    username=request.user
    feluri_mancare = Mancare.objects.filter(username_autor=username).order_by('-id')
    return render(request,
          'gallery_private.html',
          {
                'feluri_mancare':feluri_mancare,
          }
    )

# Pornire pagina 'Favorit';
def favorit(request):
    id_user = request.user.id

    id_mancaruri_favorite = list(
        Favorit.objects.filter(id_user=id_user).values_list('id_mancare', flat=True)
    )

    mancaruri_favorite = Mancare.objects.filter(id__in=id_mancaruri_favorite)

    return render(
        request,
        "favorit.html",
        {
            'mancaruri_favorite': mancaruri_favorite,
        }
    )

#  Pentru a adauga la favorit (salvare la favorit);
def salvare(request, fel_de_mancare_id):
    Mancare_object=Mancare.objects.get(pk=fel_de_mancare_id)
    user_curent = request.user

    # Verificare daca exista o mancare la favorit.
    if Favorit.objects.filter(id_mancare=Mancare_object, id_user=user_curent).exists():
        messages.info(request, "Aceasta mancare a fost deja adaugata la favorit!")
        return render(request,'error_404.html')

    # Adaugare mancare la favorit.
    favorit_object = Favorit(id_user=user_curent, id_mancare=Mancare_object, salvat=True)
    print("Done save on FAVORIT")
    favorit_object.save()
    messages.info(request, "Mancarea a fost salvata cu succes la 'Favorit'")
    return redirect('/gallery-public/')


    # TODO: Fa atunci cand dai click pe butonul salveaza sa te duca direct la href-ul unde ai apsat pe buton (ex: fel_de_mancare_id)
    # TODO:p.s: vezi daca ii poti baga animatie.

# Stergere fel de mancare de la favorit.
def delete(request, fel_mancare_id):
    user_curent = request.user

    #Verificare daca se afla la favorit
    if not Favorit.objects.filter(id_mancare = fel_mancare_id, id_user = user_curent.id).exists():
        messages.info(request, "Aceasta mancare nu se afla la favorit")
        return render(request, 'error_404.html')

    # Stergere mancare de la favorit
    Favorit.objects.filter(id_mancare=fel_mancare_id, id_user=user_curent.id).delete()
    print("Done delete image")
    messages.info(request, "Mancarea a fost stearsa.")
    return redirect('/favorit/')