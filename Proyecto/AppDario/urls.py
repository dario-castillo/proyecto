
from django.urls import path
from AppDario import views


urlpatterns = [
    path('', views.saludo, name='inicio'),
    path('tarifario/', views.tarifario, name='tarifario'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('about/', views.about, name= 'acercademi'),
    path('bocetos/', views.bocetos, name= 'bocetos'),

         
]

