from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from django.db.models.query import QuerySet
from producto.models import Cliente, Articulo, Pedidos
from typing import Any
from django.contrib import messages


def Home(request):

    return render(request,"producto/home.html")


class ArticuloList(ListView):
    model = Articulo
    context_object_name = "articulolista"
    template_name = "articulo_lista.html"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        
        if busqueda:
            if len(busqueda) < 20:
                queryset = Articulo.objects.filter(nombre__icontains=busqueda)
            else:
                # Si la búsqueda es demasiado larga, crea un mensaje de error
                messages.error(self.request, "La búsqueda es demasiado larga (máximo 20 caracteres)")
                # Devuelve el queryset original sin filtrar
                return queryset
                
        return queryset
