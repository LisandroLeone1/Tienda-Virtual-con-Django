from django.contrib import admin
from servicios.models import Servicios, Funciones

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Servicios, ServicioAdmin)
admin.site.register(Funciones)
