from django.contrib import admin
from .models import Carrera, Persona, Mensaje  # Importa tus modelos

admin.site.register(Carrera)  # Registra el modelo Carrera
admin.site.register(Persona)  # Registra el modelo Persona
admin.site.register(Mensaje)  # Registra el modelo Mensaje
