from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, UpdateView
from .forms import UsuarioForm, EditUsuarioForm
from .models import Usuario
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_not_required
from Proyecto.models import Proyecto
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # Agregar los proyectos al contexto
        context['proyectos'] = Proyecto.objects.all()  # Obtener todos los proyectos
        print(Proyecto.objects.all().values())
        return context

class UsuarioListView(ListView):
    template_name = 'Login/listado_usuario.html'
    model = Usuario
    context_object_name = 'usuario'

    def get_queryset(self):
        # Filtra los usuarios excluyendo aquellos con rol None
        return Usuario.objects.exclude(rol__isnull=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title_table'] = 'Listado de usuarios'
    
        return context



@method_decorator(login_not_required, name='dispatch')
class RegisterView(CreateView):
    template_name = 'Login/Registro.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('listado_usuario')
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['cancelar'] = reverse_lazy('listado_usuario')
    
        return context
    
    
class UsuarioEditView(UpdateView):
    template_name = 'Login/editar_usuario.html'
    model = Usuario
    form_class = EditUsuarioForm
    success_url = reverse_lazy('listado_usuario')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['cancelar'] = reverse_lazy('listado_usuario')
    
        return context