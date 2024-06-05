from django.shortcuts import render
from servicios.models import Servicios
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView

# Create your views here.
class ServiciosList(ListView):
    model = Servicios
    context_object_name = "servicios"
    template_name = "servicios_list.html"