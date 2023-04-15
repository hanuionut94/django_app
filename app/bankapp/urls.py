from django.urls import path, include
from . import views

urlspatterns = [
    path('', views.home, name='home')
]