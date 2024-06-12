from django.urls import path
from producto.views import Home
from django.conf import settings
from django.conf.urls.static import static
#from config import views

app_name = "producto"
urlpatterns = [
   path('',Home,name="home"),
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)