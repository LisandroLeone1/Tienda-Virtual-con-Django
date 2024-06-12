from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from django.db.models.query import QuerySet
from carro.carro import Carro



def Home(request):
    carro = Carro(request)
    return render(request,"producto/home.html")



