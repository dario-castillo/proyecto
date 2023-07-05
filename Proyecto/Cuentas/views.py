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
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.list import ListView

from Cuentas import forms
from Cuentas import models
from Cuentas.models import Cuenta
from Cuentas.models import Pedido
# Create your views here.

def registro(request):
    if request.method == 'POST':
        form = forms.RegistroUsuarioForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('iniciarsesion')
        else:
            return render(request, 'Cuentas/crear_cuenta.html', {'miformulario':form})
    form = forms.RegistroUsuarioForm()
    return render(request, 'Cuentas/crear_cuenta.html', {'miformulario':form})        


def loguearse(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                django_login(request, user)
                return redirect('inicio')
            else:
                return render(request, "Cuentas/iniciar_sesion.html", {"mensaje":"Datos incorrectos"})

    form = AuthenticationForm()
    return render(request, 'Cuentas/iniciar_sesion.html', {'formu_inicio':form})


class Desloguearse(LogoutView):
    template_name= 'Cuentas/desloguearse.html'

def editar_cuenta(request):
    usuario = request.user
    modelo_cuenta, _ =models.Cuenta.objetcts.get_or_create(user=usuario)
    if request.method == 'POST':
        form = forms.EditarUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('email'):
                usuario.email = data.get('email')
            if data.get('first_name'):
                usuario.first_name = data.get('first_name')
            if data.get('last_name'):
                usuario.last_name = data.get('last_name')
            modelo_cuenta.avatar = data.get('avatar') if data.get('avatar') else modelo_cuenta.avatar

            modelo_cuenta.save()
            usuario.save()
            return redirect('inicio')
        else:
            return render(request, "Cuentas/editar_cuenta.html", {"form":form})
    
    form = forms.EditarUsuarioForm(
        initial={
            'email':usuario.email,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,
            'avatar': modelo_cuenta.last_name
             }
        )
    return render(request, "Cuentas/editar_cuenta.html", {"form":form})

#class MiCuenta(ListView):
    model = Cuenta
    template_name = 'Cuentas/crud_cuenta.html'



#class VerCuenta(DetailView):
    model = Cuenta
    template_name = 'Cuentas/ver_cuenta.html'

class ListadoPedidos(ListView):
    model = Pedido
    template_name = 'Cuentas/crud_pedidos.html'

class CrearPedido(CreateView):
    model = Pedido
    template_name = 'Cuentas/crear_pedido.html'
    success_url = reverse_lazy('pedido')
    fields = '__all__'


class MostrarPedido(DetailView):
    model = Pedido
    template_name = 'Cuentas/mostrar_pedidos.html'

class EditarPedido(UpdateView):
    model = Pedido
    template_name = 'Cuentas/editar_pedidos.html'
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse_lazy('mostrarpedido', kwargs={'pk':self.object.pk})
    
class EliminarPedido(DeleteView):
    model = Pedido
    template_name = 'Cuentas/eliminar_pedido.html'
    success_url = reverse_lazy('pedido')


def eliminar_cuenta(request):
    ...

def cambiar_password(request):
    ...


