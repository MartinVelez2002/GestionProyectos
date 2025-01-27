from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .forms import SprintForm
from .models import Sprint
from django.urls import reverse_lazy

class SprintCreateView(CreateView):
    template_name = 'Sprint/crear_sprint.html'
    form_class = SprintForm
    model = Sprint
    success_url = 'listSprint'

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('listado_tarea')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
        return context


class SprintListView(ListView):
    template_name = 'Sprint/listar_sprint.html'
    model = Sprint
    context_object_name = 'sprint'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title_table'] = 'Sprint'
    
        return context