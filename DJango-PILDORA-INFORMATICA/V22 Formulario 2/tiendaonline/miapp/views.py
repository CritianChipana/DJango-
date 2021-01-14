from django.shortcuts import render,HttpResponse
from miapp.models import Articulo

# Create your views here.

def busqueda_productos(request):
    return render(request,"busqueda_productos.html")

def buscar(request):

    if request.GET['prd']:

        #mensaje="Articulo Buscado: %r"%request.GET["prd"]
        producto=request.GET['prd']
        articulos=Articulo.objects.filter(nombre__icontains=producto)
        return render(request,"resultafos_busqueda.html",{"articulos":articulos,"query":producto})
    else:
        mensaje="No has ingresado ningun valor"

    return HttpResponse(mensaje)

