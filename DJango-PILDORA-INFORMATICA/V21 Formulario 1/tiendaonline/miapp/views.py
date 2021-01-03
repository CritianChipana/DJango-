from django.shortcuts import render,HttpResponse

# Create your views here.

def busqueda_productos(request):
    return render(request,"busqueda_productos.html")

def buscar(request):
    mensaje="Articulo Buscado: %r"%request.GET["prd"]
    return HttpResponse(mensaje)



