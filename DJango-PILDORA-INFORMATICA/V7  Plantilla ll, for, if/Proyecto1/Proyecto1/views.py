from django.http import HttpResponse
import datetime
from django.template import Template,Context


class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido


def saludo(request):

    p1=Persona("Carla","Ascues")

    # nombre ="Cristian"
    # apellido ="Chipana"

    temas_curso= ["plantillas","modelos","formularios","vistas","despliegue"]

    ahora = datetime.datetime.now()
    
    doc_externo =open("C:/Users/admi/Desktop/DJango-/DJango-PILDORA-INFORMATICA/V7  Plantilla ll, for, if/Proyecto1/Proyecto1/plantillas/miplantilla.html")
    
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora, "temas":temas_curso})


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