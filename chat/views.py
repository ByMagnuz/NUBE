from django.shortcuts import render
from .models import Mensaje

def home(request):
    return render(request, 'home.html')

def messages(request):
    mensajes = Mensaje.objects.all().order_by('id')
    return render(request, 'messages.html', {'mensajes': mensajes})
