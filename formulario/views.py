from django.shortcuts import render, redirect
from .forms import InscripcionForm

def inscripcion_view(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            inscripcion = form.save(commit=False)  # No guardar aún
            inscripcion.save()  # Guarda la inscripción
            form.save_m2m()  # Guarda la relación de ManyToMany
            return redirect('gracias')  # Redirige a una página de agradecimiento
    else:
        form = InscripcionForm()

    return render(request, 'formulario/inscripcion.html', {'form': form})


def gracias_view(request):
    return render(request, 'formulario/gracias.html')
