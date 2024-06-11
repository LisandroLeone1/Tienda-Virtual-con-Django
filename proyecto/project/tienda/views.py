from django.shortcuts import render
from .models import Producto, CategoriaProducto
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from django.db.models import Q

class TiendaList(ListView):
    model = Producto
    context_object_name = "producto"
    template_name = "producto_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Producto.objects.filter(Q(nombre__icontains=busqueda) | Q(marca__icontains=busqueda))
        return queryset

def categoria_producto(request, categoria_id):
    categoria = CategoriaProducto.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categorias=categoria)
    categorias_unicas = CategoriaProducto.objects.filter(categoria__in=productos).distinct()
    return render(request, "tienda/tienda_categoria.html", {'categoria': categoria, 'categorias_unicas': categorias_unicas,'productos:': productos})

