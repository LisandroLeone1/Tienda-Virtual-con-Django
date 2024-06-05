from django.urls import path
from blog.views import PostList, categoria

app_name = "blog"

urlpatterns = [
    path('', PostList.as_view(), name="blog"),
    path('categoria/<int:categoria_id>',categoria,name="categoria")
]