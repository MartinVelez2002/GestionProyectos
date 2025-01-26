from django.urls import path
from .views import *


urlspatterns = [
    path('crear_proyecto/', ProyectoCreateView.as_view(), name='createProject'),
    path('listar_proyecto/', ProyectoCreateView.as_view(), name='listProject'),
]