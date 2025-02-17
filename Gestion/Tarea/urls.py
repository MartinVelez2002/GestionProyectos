from django.urls import path
from .views import *
urlpatterns = [
    path('tareas', TareaListView.as_view(), name='listado_tarea'),
    path('crear_tareas/', TareaCreateView.as_view(), name='crear_tarea'),
    path('detalle_tarea/<int:pk>', TareaDetailView.as_view(), name='detalle_tarea'),
]