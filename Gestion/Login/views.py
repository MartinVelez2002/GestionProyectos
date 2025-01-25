from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView
from .forms import UsuarioForm
from .models import Usuario
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_not_required

class HomeView(TemplateView):
    template_name = 'home.html'


class UsuarioListView(ListView):
    template_name = 'Login/listado_usuario.html'
    model = Usuario
    context_object_name = 'usuario'

    def get_queryset(self):
        # Filtra los usuarios excluyendo aquellos con rol None
        return Usuario.objects.exclude(rol__isnull=True)

@method_decorator(login_not_required, name='dispatch')
class RegisterView(CreateView):
    template_name = 'Login/Registro.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('listado_usuario')
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['cancel'] = reverse_lazy('listado_usuario')
    
        return context