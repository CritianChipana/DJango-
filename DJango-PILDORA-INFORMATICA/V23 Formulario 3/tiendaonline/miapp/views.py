from django.shortcuts import render,HttpResponse
from miapp.models import Articulo
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def busqueda_productos(request):
    return render(request,"busqueda_productos.html")

def buscar(request):

    if request.GET['prd']:

        #mensaje="Articulo Buscado: %r"%request.GET["prd"]
        producto=request.GET['prd']

        if len(producto)>20:
            mensaje="Texto muy largo"
        else:
            articulos=Articulo.objects.filter(nombre__icontains=producto)
            return render(request,"resultafos_busqueda.html",{"articulos":articulos,"query":producto})
    else:
        mensaje="No has ingresado ningun valor"

    return HttpResponse(mensaje)


def contacto(request):

    if request.method == "POST":

        subject =request.POST['asunto']
        message =request.POST['mensaje']+ " " + request.POST['email']
        email_from=settings.EMAIL_HOST_USER
        recipiente = ["74309273@untels.edu.pe"]
        send_mail(subject,message,email_from,recipiente)

        return render(request,"gracias.html")
    return render(request,"contacto.html")