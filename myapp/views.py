from django.shortcuts import render

from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=255)
    telefono = models.DecimalField(max_digits=10, decimal_places=0)

