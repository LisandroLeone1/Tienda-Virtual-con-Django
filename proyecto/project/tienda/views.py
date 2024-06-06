from django.shortcuts import render
from .models import Producto, CategoriaProducto
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from django.db.models import Q

class TiendaList(ListView):
    model = Producto
    context_object_name = "producto"
    template_name = "producto_list.html"

def categoria_producto(request, categoria_id):
    categoria = CategoriaProducto.objects.get(id=categoria_id)
    producto = Producto.objects.filter(categorias = categoria)
    return render(request,"tienda/tienda_categoria.html",{'categoria': categoria, 'producto':producto})