from django.shortcuts import render
from blog.models import Post, Categoria
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView

# Create your views here.
class PostList(ListView):
    model = Post
    context_object_name = "post"
    template_name = "post_list.html"


def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    post = Post.objects.filter(categorias = categoria)
    return render(request,"blog/categoria.html",{'categoria': categoria, 'post':post})
