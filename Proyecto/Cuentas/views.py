from django.shortcuts import render
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, LogoutView

from django.views.generic import DeleteView

from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from Cuentas import forms
from Cuentas import models
# Create your views here.

def registro(request):
    if request.method == 'POST':
        form = forms.RegistroUsuarioForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'Cuentas/crear_cuenta.html', {'miformulario':form})
    form = forms.RegistroUsuarioForm()
    return render(request, 'Cuentas/crear_cuenta.html', {'miformulario':form})        


def login_request(request):
    ...

def editar_cuenta(request):
    ...

def mostrar_cuenta(request):
    ...
def eliminar_cuenta(request):
    ...

def cambiar_password(request):
    ...


