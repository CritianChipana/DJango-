from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30,verbose_name="La direccion")
    email=models.EmailField(blank=True,null=True)
    tfno=models.CharField(max_length=9)

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return "el nombre es: %s, la seccion es: %s, el precio es: %s" % (self.nombre,self.seccion,self.precio)

class Pedido(models.Model):
    numero=models.IntegerField()
    fecha=models.DateTimeField()
    entregado=models.BooleanField()