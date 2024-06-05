from django.contrib import admin
from servicios.models import Servicios

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Servicios, ServicioAdmin)
