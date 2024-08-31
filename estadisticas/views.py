from django.shortcuts import render
from django.db.models import Count
from formulario.models import Inscripcion
import matplotlib.pyplot as plt
import io
import urllib, base64

def estadisticas_view(request):
    # Obtener los datos de inscripciones agrupados por curso
    datos = Inscripcion.objects.values('curso__nombre').annotate(total=Count('curso')).order_by('-total')

    # Nombres de los cursos y sus correspondientes cantidades
    cursos = [dato['curso__nombre'] for dato in datos]
    cantidades = [dato['total'] for dato in datos]

    # Generar el gráfico
    plt.figure(figsize=(10, 5))
    plt.bar(cursos, cantidades, color='skyblue')
    plt.xlabel('Cursos')
    plt.ylabel('Cantidad de Inscripciones')
    plt.title('Estadísticas de Inscripciones por Curso')

    # Convertir el gráfico en una imagen que se pueda incrustar en HTML
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return render(request, 'estadisticas/estadisticas.html', {'data': uri})
