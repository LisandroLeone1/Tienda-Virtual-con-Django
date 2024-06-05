from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50,verbose_name="La direccion")
    email = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return f'cliente {self.nombre}, email {self.email}'

class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.CharField(max_length=50)
    precio = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.nombre

class Pedidos(models.Model):
    numero = models.IntegerField(default=0)
    fecha = models.DateField(null=True,blank=True)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.numero



