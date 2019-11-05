# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Mancare(models.Model):
    titlul= models.CharField(max_length=50)
    descriere= models.CharField(max_length=300)
    upload = models.FileField(upload_to='static/img/')
