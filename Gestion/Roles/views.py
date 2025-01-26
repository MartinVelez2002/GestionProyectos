from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from .forms import RolesForm
from django.contrib.auth.models import Group
from django.urls import reverse_lazy


class RolesListView(ListView):
    template_name = 'Rol/listado_rol.html'
    context_object_name = 'rol'
    model = Group
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title_table'] = 'Listado de roles y permisos'
        return context

class RolesCreateView(CreateView):
    template_name = 'Rol/crear_rol.html'
    form_class = RolesForm
    success_url = reverse_lazy('listRol')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['cancelar'] = reverse_lazy('listRol')
    
        return context
    
    
    def form_valid(self, form):
        group = form.save()

        permissions = form.cleaned_data['permissions']
        group.permissions.set(permissions)

        return super().form_valid(form)

class RolEditView(UpdateView):
    template_name = 'Rol/crear_rol.html'
    model = Group
    form_class = RolesForm
    success_url = reverse_lazy('listRol')
    
    def form_valid(self, form):
        group = form.save()

        permissions = form.cleaned_data['permissions']
        group.permissions.set(permissions)

        return super().form_valid(form)
    