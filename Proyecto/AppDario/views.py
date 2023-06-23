from django.http import HttpResponse
from django.shortcuts import render
from .models import Tarifario
from .models import Newsletters

def saludo(request):
   # return HttpResponse("Hola Darío")

    return render(request, "AppDario/index.html")
 
def tarifario(request):
    
    if request.method == 'POST':
        tarifario = Tarifario(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'])
        tarifario.save()    
        return render(request, "AppDario/index.html")
    
    return render(request, "AppDario/tarifario.html")

def newsletter(request):
    if request.method == 'POST':
        newsletters = Newsletters(nombre=request.POST['nombre'], email=request.POST['email'])
        newsletters.save()    
        return render(request, "AppDario/index.html")


    return render(request, "AppDario/newsletter.html")

