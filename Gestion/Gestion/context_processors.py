from django.contrib.auth.models import AnonymousUser


def user_info(request):
    if request.user and not isinstance(request.user, AnonymousUser):
        # Inicializamos el contexto con información del usuario autenticado
        context = {
            'nombre': request.user.first_name,
            'apellido': request.user.last_name,
            'cedula': getattr(request.user, 'cedula', None),  # Recupera la cédula si existe
            'grupo': request.user.groups.name if request.user.groups else None,  # Nombre del grupo (rol)
        }
    else:
        # Contexto vacío para usuarios no autenticados
        context = {
            'nombre': None,
            'apellido': None,
            'cedula': None,
            'grupo': None,
        }

    return context
