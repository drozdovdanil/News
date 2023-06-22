from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .filters import PostFilter
from .forms import PostForm
from .models import Post


class ProductsList(ListView):
    model = Post
    ordering = '-time_post'
    template_name = 'post.html'
    context_object_name = 'post'
    paginate_by = 5


class ProductDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'pos.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'


class PostDetail(ListView):
    model = Post
    ordering = '-time_post'
    template_name = 'search.html'
    context_object_name = 'post'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(PermissionRequiredMixin, CreateView):
    # Указываем нашу разработанную форму
    form_class = PostForm
    permission_required = ('news.add_post',)
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/post/article/create/':
            post.type_1 = 'AR'
        post.save()
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.change_post',)


class PostDelete(DeleteView):
    model = Post
    template_name = 'product_delete.html'
    success_url = reverse_lazy('post')


class LoginView(ListView):
    model = Post
    template_name = 'login.html'
    context_object_name = 'login'