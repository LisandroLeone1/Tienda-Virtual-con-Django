from django.urls import path
from login.views import index, CustomLoginViews, register
from django.contrib.auth.views import LogoutView

app_name = "login"

urlpatterns = [
    path("''", CustomLoginViews.as_view(), name="login"),
    path("logout/",LogoutView.as_view(template_name = "core/logout.html"), name="logout"),
    path("register/",register,name="register")
]