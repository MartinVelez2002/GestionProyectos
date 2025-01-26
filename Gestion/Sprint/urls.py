from django.urls import path
from .views import *


urlpatterns = [
    path('crear_sprint/', SprintCreateView.as_view(), name='createSprint'),
    path('listar_sprint/', SprintListView.as_view(), name='listSprint'),
]