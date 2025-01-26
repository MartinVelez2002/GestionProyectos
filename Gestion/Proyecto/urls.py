from django.urls import path
from .views import *


urlpatterns = [
    path('crear_proyecto/', ProyectoCreateView.as_view(), name='createProject'),
    path('listar_proyecto/', ProyectoListView.as_view(), name='listProject'),
]