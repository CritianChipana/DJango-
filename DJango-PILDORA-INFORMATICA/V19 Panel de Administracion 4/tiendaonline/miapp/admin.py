from django.contrib import admin
from miapp.models import Cliente,Articulo,Pedido


# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","tfno") # transforma los objetos a informacion en formato tabla
    search_fields=("nombre","tfno") #Crea un textFiel para buscar con los campos llamados

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)


class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"

admin.site.register(Cliente,ClientesAdmin) #Si se crea listas 
admin.site.register(Articulo,ArticulosAdmin)
admin.site.register(Pedido,PedidosAdmin)





