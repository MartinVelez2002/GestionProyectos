from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .forms import TareaForm, ComentarioForm
from .models import Tarea, Comentario
from django.urls import reverse_lazy


# Create your views here.

class TareaCreateView(CreateView):
    template_name = 'Tarea/crear_tarea.html'
    form_class = TareaForm
    model = Tarea

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('listado_tarea')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
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


from django.urls import reverse
from django.shortcuts import get_object_or_404


class TareaDetailView(DetailView):
    template_name = 'Tarea/detalle_tarea.html'
    model = Tarea
    context_object_name = 'tarea'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formulario'] = ComentarioForm()
        context['comentarios'] = Comentario.objects.filter(Tarea_id=self.kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        # Obtener la instancia de la tarea actual
        self.object = self.get_object()
        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.Personal = request.user  # Asocia el usuario actual
            comentario.Tarea = self.object  # Asocia la tarea actual
            comentario.save()
            # Redirige a la misma página después de guardar
            return redirect('detalle_tarea', pk=self.object.pk)
        else:
            # Si el formulario no es válido, renderiza nuevamente con errores
            context = self.get_context_data()
            context['formulario'] = form
            return self.render_to_response(context)
