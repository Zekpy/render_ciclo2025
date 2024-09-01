from django.shortcuts import render, redirect
from .forms import InscripcionForm
from cursos.models import Categoria  # Importar la categoría

def inscripcion_view(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            inscripcion = form.save(commit=False)
            inscripcion.save()
            form.save_m2m()
            return redirect('gracias')
    else:
        form = InscripcionForm()

    categorias = Categoria.objects.all()  # Obtener todas las categorías
    context = {
        'form': form,
        'categorias': categorias  # Pasar las categorías al template
    }
    return render(request, 'formulario/inscripcion.html', context)



def gracias_view(request):
    return render(request, 'formulario/gracias.html')
