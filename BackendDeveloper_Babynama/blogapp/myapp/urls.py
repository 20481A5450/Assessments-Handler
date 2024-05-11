from django.urls import path
from . import views

path = [
    path('', views.index, name='index'),
]