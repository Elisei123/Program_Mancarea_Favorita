# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Mancare(models.Model):
    titlul=models.CharField(max_length=20)
    descriere=models.CharField(max_length=300)
    upload=models.ImageField(upload_to='images/')
    username_autor=models.CharField(max_length=50, default='NON Autor')
    data_publicarii=models.CharField(max_length=50, default='NON Data')

