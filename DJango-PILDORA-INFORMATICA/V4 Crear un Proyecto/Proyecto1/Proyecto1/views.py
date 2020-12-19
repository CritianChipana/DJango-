from django.http import HttpResponse
import datetime

def saludo(request):
    menaje ="Esto es un saludo desde una variable de paiton"
    return HttpResponse(menaje)


def despedida(request):
    return HttpResponse("adios mmgv")

def damefecha(request):
    fecha_actual = datetime.datetime.now()
    mensaje= """
                La fecha actual es %s
                """%fecha_actual
    return HttpResponse(mensaje)

def calcular(request,ano,b):
    b=18
    # adadactual=18
    perioda = ano-2020
    edadfutura = b + perioda

    documento = f"en el año '{ano}' tendras '{edadfutura}' años "
    return HttpResponse(documento)