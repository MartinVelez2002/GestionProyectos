from django.urls import path
from .views import *
urlpatterns = [
    path('listado_rol/', RolesListView.as_view(), name='listRol'),
    path('crear_rol/', RolesCreateView.as_view(), name='createRol')
]