from django.shortcuts import render
from django.contrib.auth.views import LoginView

class LoginView(LoginView):
    template_name = 'tareas/login.html'  # Ruta al archivo de plantilla de login


def base(request):
    return render(request, 'tareas/base.html')

# Create your views here.
