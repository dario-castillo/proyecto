from django.urls import path
from Cuentas import views


urlpatterns = [
    path('registro/', views.registro, name='registro'),
]