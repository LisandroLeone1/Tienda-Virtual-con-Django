from django.urls import path
from servicios.views import ServiciosList

app_name = "servicios"

urlpatterns = [
    path('', ServiciosList.as_view(), name="servicios"),
]