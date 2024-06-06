from django.shortcuts import render, HttpResponse, redirect
from .forms import ContactoForms

def Contacto(request):
    formulario_contacto = ContactoForms()
    if request.method == "POST":
        formulario_contacto = ContactoForms(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            return redirect("/contacto/?valido")

    return render(request,"contacto/contacto.html",{"miFormulario":formulario_contacto})

