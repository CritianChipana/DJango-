from django.contrib import admin
from miapp.models import Cliente,Articulo,Pedido


# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","tfno")
    search_fields=("nombre","tfno")


admin.site.register(Cliente,ClientesAdmin)
admin.site.register(Articulo)
admin.site.register(Pedido)





