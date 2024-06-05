from django.urls import path
from producto.views import ArticuloList, Home, Tienda
from django.conf import settings
from django.conf.urls.static import static
#from config import views

app_name = "producto"
urlpatterns = [
   path('',Home,name="home"),
   path('tienda/',Tienda,name="tienda"),
   path("articulo/",ArticuloList.as_view(), name="articulo_lista"),
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)