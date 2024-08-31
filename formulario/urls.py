from django.urls import path
from .views import inscripcion_view, gracias_view

urlpatterns = [
    path('inscripcion/', inscripcion_view, name='inscripcion'),
     path('gracias/', gracias_view, name='gracias'),
]
