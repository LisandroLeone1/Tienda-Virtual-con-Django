def importe_total_carro(request):
    total = 150
    if request.user.is_authenticated:
        carro = request.session.get("carro", {})  # Obtener el diccionario de carro de la sesión
        for key, value in carro.items():  # Iterar sobre las claves y valores del diccionario
            total += float(value["precio"]) * value["cantidad"]  # Calcular el total
    return {"importe_total_carro": total}