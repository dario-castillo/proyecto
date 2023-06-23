from django.http import HttpResponse
from django.shortcuts import render
from .models import Tarifario
from .models import Newsletters
from .models import Cursos
from .forms import BuscaCursoForm


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

def buscar_curso(request):
    if request.method == 'POST':
        busca_curso = BuscaCursoForm(request.POST)

        if busca_curso.is_valid():
            info = busca_curso.cleaned_data
            cursos = Cursos.objects.filter(nombre=info["curso"])
            return render(request, "AppDario/lista.html", {"cursos": cursos})
    else:
        busca_curso = BuscaCursoForm()
        return render(request, "AppDario/buscar_curso.html", {"miFormulario": buscar_curso})
    
