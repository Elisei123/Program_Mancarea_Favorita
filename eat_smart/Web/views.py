# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def login(request):
    print('esti in login')
    return render(request, 'login.html')

def register(request):
    print('esti in register')
    return render(request, 'register.html')
