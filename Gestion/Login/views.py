from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import UsuarioForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_not_required

class HomeView(TemplateView):
    template_name = 'home.html'


@method_decorator(login_not_required, name='dispatch')
class RegisterView(CreateView):
    template_name = 'Login/Registro.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')
    
    
    