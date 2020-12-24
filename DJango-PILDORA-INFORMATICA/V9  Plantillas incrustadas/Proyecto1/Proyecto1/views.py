from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template import loader
from django.shortcuts import render


class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido


def saludo(request):

    p1=Persona("Carla","Ascues")

    temas_curso= ["plantillas","modelos","formularios","vistas","despliegue"]

    ahora = datetime.datetime.now()

    #doc_externo = loader.get_template('miplantilla.html'), 2017230428
 

    ctx=({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora, "temas":temas_curso})
    
    # documento = doc_externo.render(ctx)
    # return HttpResponse(documento)
    return render(request,"miplantilla.html",ctx)


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