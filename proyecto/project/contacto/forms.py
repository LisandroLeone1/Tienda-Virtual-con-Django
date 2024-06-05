from django import forms
from . import models

class ContactoForms(forms.Form):
    nombre = forms.CharField(label="Nombre",required=True)
    email = forms.CharField(label="Email",required=True)
    contenido = forms.CharField(label="Contenido")
       