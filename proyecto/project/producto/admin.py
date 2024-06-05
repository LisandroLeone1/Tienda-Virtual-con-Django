from django.contrib import admin
from producto.models import Cliente, Pedidos, Articulo


class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre",
                  "direccion",
                  "email",
                  "telefono") # Vista en panel de administracion
    search_fields=("nombre","email") #Barra de busqueda
    list_filter=("nombre","direccion") #Filtrar por nombre y direccion

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Pedidos)
admin.site.register(Articulo)
