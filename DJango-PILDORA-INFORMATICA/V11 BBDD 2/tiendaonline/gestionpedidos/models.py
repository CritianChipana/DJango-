from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30)
    email=models.EmailField()
    tfno=models.CharField(max_length=9)


class Articulo(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio = models.IntegerField()

class Pedido(models.Model):
    numero=models.IntegerField()
    fecha=models.DateTimeField()
    entregado=models.BooleanField()