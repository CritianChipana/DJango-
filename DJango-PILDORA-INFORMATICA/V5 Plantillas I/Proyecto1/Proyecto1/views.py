from django.http import HttpResponse
import datetime
from django.template import Template,Context


def saludo(request):
    # C:\Users\admi\Desktop\DJango-\DJango-PILDORA-INFORMATICA\V5 Plantillas I\Proyecto1\Proyecto1
    
    doc_externo =open("C:/Users/admi/Desktop/DJango-/DJango-PILDORA-INFORMATICA/V5 Plantillas I/Proyecto1/Proyecto1/plantillas/miplantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento = plt.render(ctx)

    return HttpResponse(documento)


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