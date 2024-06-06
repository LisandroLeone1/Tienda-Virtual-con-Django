from django.urls import path
from tienda.views import TiendaList, categoria_producto


app_name = "tienda"
urlpatterns = [
   path('',TiendaList.as_view(),name="tienda"),
   path('tienda/categoria/<int:categoria_id>',categoria_producto,name="categoria_producto")
]