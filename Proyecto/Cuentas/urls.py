from django.urls import path
from Cuentas import views


urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('iniciarsesion/', views.loguearse, name='iniciarsesion'),
    path('salir/', views.Desloguearse.as_view(), name='salir'),

]