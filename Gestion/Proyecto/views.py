from django.shortcuts import render

from Sprint.models import Sprint
from .forms import ProyectoForm
from .models import Proyecto
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from Tarea.models import Tarea


class ProyectoCreateView(CreateView):
    template_name = 'Proyecto/crear_proyecto.html'
    form_class = ProyectoForm
    model = Proyecto
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancelar'] = reverse_lazy('home')
        return context


class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'Proyecto/detalle_Proyecto.html'
    context_object_name = 'proyecto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener los sprints asociados al proyecto
        context['sprint'] = Sprint.objects.filter(Proyecto=self.object)

        # Obtener las tareas asociadas a los sprints del proyecto
        sprints_del_proyecto = Sprint.objects.filter(Proyecto=self.object)
        context['tarea'] = Tarea.objects.filter(Sprint__in=sprints_del_proyecto)

        return context


class ProyectoListView(ListView):
    template_name = 'Proyecto/listar_proyecto.html'
    model = Proyecto
    context_object_name = 'proyecto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title_table'] = 'Proyecto'

        return context
