from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
   # return HttpResponse("Hola Darío")

    return render(request, "AppDario/index.html")
 
def tarifario(request):
    return render(request, "AppDario/tarifario.html")

def newsletter(request):
    return render(request, "AppDario/newsletter.html")

