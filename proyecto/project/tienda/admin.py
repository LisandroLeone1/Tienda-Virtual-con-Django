from django.contrib import admin
from .models import CategoriaProducto, Producto

class CategoriaAdmin(admin.ModelAdmin): # especifica que estos campos son solo para lectura en el panel de administracion
    readonly_fields = ('created','updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(CategoriaProducto, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)


