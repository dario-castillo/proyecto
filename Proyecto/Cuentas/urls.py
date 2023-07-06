from django.urls import path
from Cuentas import views


urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('iniciarsesion/', views.loguearse, name='iniciarsesion'),
    path('vercuenta/', views.ver_cuenta, name='vercuenta'),
    path('vercuenta/editarcuenta/', views.editar_cuenta, name='editarcuenta'),
    path('vercuenta/cambiarcontraseña/', views.CambiarContraseña.as_view(), name='cambiarcontraseña'),
    path('vercuenta/eliminarcuenta/<int:pk>/', views.EliminarCuenta.as_view(), name='eliminarcuenta'),
    path('salir/', views.Desloguearse.as_view(), name='salir'),
    path('pedido/', views.ListadoPedidos.as_view(), name='pedido'),
    path('crearpedido/', views.CrearPedido.as_view(), name='crearpedido'),
    path('mostrarpedido/<int:pk>/', views.MostrarPedido.as_view(), name='mostrarpedido'),
    path('editarpedido/<int:pk>/', views.EditarPedido.as_view(), name='editarpedido'),
    path('eliminarpedido/<int:pk>/', views.EliminarPedido.as_view(), name='eliminarpedido'),

]