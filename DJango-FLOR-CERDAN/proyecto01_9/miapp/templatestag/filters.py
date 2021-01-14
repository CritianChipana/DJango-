import re
from django import template

register=template.Library()

@register.filter(name='rango')

def rango(valor):
    return f"<p style='color:red;'>Este mensaje es de la carpeta filter {valor}</p>"