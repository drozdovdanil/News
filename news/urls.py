from django.urls import path
# Импортируем созданное нами представление
from .views import *


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', ProductsList.as_view(), name='post'),
   path('<int:pk>', ProductDetail.as_view(), name='post_detail'),
   path('search/', PostDetail.as_view()),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('article/create/', PostCreate.as_view()),
   path('article/<int:pk>/update/', PostUpdate.as_view()),
   path('article/<int:pk>/delete/', PostDelete.as_view()),
   path('<int:pk>/update/login/', LoginView.as_view()),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribers', subscribe, name='subscribe')
]