from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .forms import TareaForm, ComentarioForm
from .models import Tarea, Comentario
from django.urls import reverse_lazy

# Create your views here.

class TareaCreateView(CreateView):
    template_name = 'Tarea/crear_tarea.html'
    form_class = TareaForm
    model = Tarea
    success_url = reverse_lazy('listado_tarea')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['cancelar'] = reverse_lazy('listado_tarea')
    
        return context

class TareaListView(ListView):
    template_name = 'Tarea/listar_tarea.html'
    context_object_name = 'tarea'
    model = Tarea
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title_table'] = 'Listado de Tareas'
        return context

class TareaUpdateView(UpdateView):
    template_name = 'Tarea/listar_tarea.html'
    form_class = TareaForm
    model = Tarea
    success_url = reverse_lazy('listado_tarea')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['cancelar'] = reverse_lazy('listado_tarea')
    
        return context