from django.urls import path
from Cuentas import views


urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('iniciarsesion/', views.loguearse, name='iniciar_sesion'),
    path('salir/', views.Desloguearse.as_view(), name='salir'),

]