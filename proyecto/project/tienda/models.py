from django.db import models


class CategoriaProducto(models.Model):
    categoria = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.categoria

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50,null=True,blank=True)
    categorias  = models.ManyToManyField(CategoriaProducto)
    imagen = models.ImageField(upload_to='tienda',null=True,blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.nombre