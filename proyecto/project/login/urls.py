from django.urls import path
from login.views import CustomLoginViews, register, cerrar_sesion
from django.contrib.auth.views import LogoutView

app_name = "login"

urlpatterns = [
    path("''", CustomLoginViews.as_view(), name="login"),
    path("logout/",cerrar_sesion, name="logout"),
    path("register/",register,name="register")
]