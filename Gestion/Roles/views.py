from django.shortcuts import render
from django.views.generic import CreateView
from .forms import RolesForm
# Create your views here.
class RolesView(CreateView):
    template_name = ''
    form_class = RolesForm
    