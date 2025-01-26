from django.shortcuts import render
from .forms import ProyectoForm
from .models import Proyecto
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView


class ProyectoCreateView(CreateView):
    template_name = 'Proyecto/crear_proyecto.html'
    form_class = ProyectoForm
    model = Proyecto
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancelar'] = reverse_lazy('home')
        return context


class ProyectoListView(ListView):
    template_name = 'Proyecto/listar_proyecto.html'
    model = Proyecto
    context_object_name = 'proyecto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title_table'] = 'Proyecto'

        return context
