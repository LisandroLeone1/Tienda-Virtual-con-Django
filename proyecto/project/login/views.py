from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import logout

def index(request):
    return render(request,"core/index.html")

class CustomLoginViews(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "login/login.html"

def register(request: HttpRequest):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "producto/home.html", {"mensaje": f"Usuario '{username}' creado correctamente"})
    else:
        form = CustomUserCreationForm
    return render(request, "login/register.html",{"form": form})


def cerrar_sesion(request):
    logout(request)
    
    return redirect("producto:home")
    