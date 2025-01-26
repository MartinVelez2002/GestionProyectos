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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancelar'] = reverse_lazy('listSprint')
    
        return context


class SprintListView(ListView):
    template_name = 'Sprint/listar_sprint.html'
    model = Sprint
    context_object_name = 'sprint'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title_table'] = 'Sprint'
    
        return context