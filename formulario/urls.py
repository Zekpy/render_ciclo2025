from django.urls import path
from .views import inscripcion_view, gracias_view, inicio_views

urlpatterns = [
    path('votacion/', inscripcion_view, name='votacion'),
    path('gracias/', gracias_view, name='gracias'),
    path('', inicio_views, name='inicio'),
]
