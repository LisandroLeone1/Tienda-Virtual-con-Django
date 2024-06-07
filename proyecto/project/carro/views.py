from django.shortcuts import render, redirect, HttpResponse
from .carro import Carro        
from tienda.models import Producto

def carro(request):
    return render(request,"carro/carro.html")

def agregar_producto(request,producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.agregar(producto=producto)
    return render(request,"carro/carro.html",{'carro': carro, 'producto':producto})

def eliminar_producto(request,producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.eliminar(producto=producto)
    return render(request,"carro/carro.html",{'carro': carro, 'producto':producto})

def restar_producto(request,producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.restar_producto(producto=producto)
    return render(request,"carro/carro.html",{'carro': carro, 'producto':producto})
    

def limpiar_carro(request,producto_id):
    carro = Carro(request)
    carro.limpar_carro()
    return redirect("tienda")




