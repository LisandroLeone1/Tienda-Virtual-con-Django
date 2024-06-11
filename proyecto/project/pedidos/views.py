from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from carro.carro import Carro
from pedidos.models import LineaPedido, Pedido

@login_required(login_url="/login/")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(

            producto_id = key,
            cantidad = value["cantidad"],
            user = request.user.username,
            pedido = pedido
        ))

    LineaPedido.objects.bulk_create(lineas_pedido)

    messages.success(request,"El pedido se ha creado correctamente")

    return redirect("tienda")




