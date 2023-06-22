from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
   # return HttpResponse("Hola Darío")

    return render(request, "AppDario/index.html")

