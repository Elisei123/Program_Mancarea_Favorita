# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Mancare, Favorit, Like_per_meal
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
        messages.info(request, "Ai incarcat o mancare!")
        print("Adaugare mancare")
        return redirect('gallery_private')
    else:
        return render(request, 'add-eat.html')

def gallery_public(request):
    username_curent = request.user.username

    feluri_mancare = Mancare.objects.all().order_by('-id')
    mancaruri_likes_objects = Like_per_meal(id_user=request.user)
    id_mancaruri_cu_like = list(
        Like_per_meal.objects.filter(id_user=request.user, salvat=True).values_list('id_mancare', flat=True)
    )

    for fel_mancare in feluri_mancare:
        bool_este_sau_nu_like = fel_mancare.id in id_mancaruri_cu_like
        fel_mancare.este_cu_like = bool_este_sau_nu_like


    id_mancaruri_favorite = list(
        Favorit.objects.filter(id_user=request.user.id, salvat=True).values_list('id_mancare', flat=True)
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
            'mancaruri_likes_objects':mancaruri_likes_objects,
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
        Favorit.objects.filter(id_user=id_user, salvat=True).values_list('id_mancare', flat=True)
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
    if not Favorit.objects.filter(id_mancare=Mancare_object, id_user=user_curent).exists():
        favorit_object = Favorit(id_user=user_curent, id_mancare=Mancare_object, salvat=True)
        # print("Done save on FAVORIT") # Test adaugare la favorit
        favorit_object.save()
        messages.info(request, "Mancarea a fost salvata cu succes la 'Favorit'")
        return redirect('/gallery-public/')

    # Daca nu este salvata.
    if not Favorit.objects.filter(id_user=user_curent, id_mancare=Mancare_object, salvat=True):
        Favorit.objects.filter(id_user=user_curent, id_mancare=Mancare_object).update(salvat=True)
        # print("Salvat = true") #Test True
        messages.info(request, "Mancarea a fost salvata cu succes la 'Favorit'")
        return redirect('/gallery-public/')

    # Daca este salvata la favorit, o va sterge (salvat=False)
    Favorit.objects.filter(id_user=user_curent, id_mancare=Mancare_object).update(salvat=False)
    # print("Salvat = False")    #Test Fals
    messages.info(request, "Mancarea eliminata cu succes de la 'Favorit'")
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
    Favorit.objects.filter(id_mancare=fel_mancare_id, id_user=user_curent.id).update(salvat=False)
    print("Done delete image")
    messages.info(request, "Mancarea a fost stearsa.")
    return redirect('/favorit/')


# ADD like din "Public Gallery" (inima - like)
def add_like(request, add_like_meal):
    user_curent = request.user

    # Daca nu se afla deloc obiectul add_like in lista
    Mancare_obj = Mancare.objects.get(pk=add_like_meal) # pick object mancare
    if not Like_per_meal.objects.filter(id_mancare=Mancare_obj, id_user=user_curent.id).exists():
        obj_mancare_like = Like_per_meal(id_mancare=Mancare_obj, id_user=user_curent, salvat=True)
        obj_mancare_like.save()
        return redirect('gallery_public')


    # Daca salvat=FALSE si o sa fie TRUE
    if not Like_per_meal.objects.filter(id_mancare=Mancare_obj, id_user=user_curent.id, salvat=True).exists():
        Like_per_meal.objects.filter(id_mancare=Mancare_obj, id_user=user_curent.id).update(salvat=True)
        return redirect('gallery_public')

    # Daca salvat=TRUE si o sa fie FALSE
    Like_per_meal.objects.filter(id_mancare=Mancare_obj, id_user=user_curent.id).update(salvat=False)
    return redirect('gallery_public')

