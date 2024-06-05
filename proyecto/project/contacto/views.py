from django.shortcuts import render, HttpResponse
from .forms import ContactoForms

def Contacto(request):
    formulario_contacto = ContactoForms()

    return render(request,"contacto/contacto.html",{"miFormulario":formulario_contacto})

