from typing import DefaultDict
from django.db import models

# Create your models here.

class Articulo(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    imagen = models.ImageField(default = 'null')
    publicado = models.BooleanField()
    # AUTO_NOW_ADD=true, -> me permite registrar lafecha de creacion del registro
    creado = models.DateTimeField(auto_now_add=True)
    # ayto_now=true, me permite registrar la fecha cuando se modificaque el registro
    actualizado = models.DateTimeField(auto_now=True)


class Categoria(models.Model):
    nombre = models.CharField(max_length=115)
    descripcion = models.CharField(max_length=250)
    # models.datafield(), para guardar la fecha de manera manual
    creado = models.DateField()

