from django.views.generic import ListView, DetailView
from .models import Post


class ProductsList(ListView):
    model = Post
    ordering = '-text_news'
    template_name = 'post.html'
    context_object_name = 'post'


class ProductDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'pos.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'
