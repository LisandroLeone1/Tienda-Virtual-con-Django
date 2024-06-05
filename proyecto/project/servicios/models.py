from django.db import models

class Funciones(models.Model):
    funcion = models.CharField(max_length=200)

    def __str__(self):
        return self.funcion
    
    
class Servicios(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.ManyToManyField(Funciones)
    imagen = models.ImageField(null=True,blank=True,upload_to='servicios') # le indicamos que se guarde en la subcarpeta servicios
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.titulo
