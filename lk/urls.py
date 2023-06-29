from django.urls import path
from .views import Lk

urlpatterns = [
    path('', Lk.as_view()),
]