from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('registro/', RegisterView.as_view(), name='register'),
    path('listado/', UsuarioListView.as_view(), name='listado_usuario')
]