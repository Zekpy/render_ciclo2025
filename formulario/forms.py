from django import forms
from .models import Inscripcion

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['nombre', 'apellido', 'celular', 'email', 'edad', 'cursos']
    
    def clean(self):
        cleaned_data = super().clean()
        celular = cleaned_data.get('celular')
        email = cleaned_data.get('email')

        # Validar que el celular no esté ya registrado
        if Inscripcion.objects.filter(celular=celular).exists():
            self.add_error('celular', 'Este número de celular ya ha sido utilizado para Votar.')

        # Validar que el email no esté ya registrado
        if Inscripcion.objects.filter(email=email).exists():
            self.add_error('email', 'Este correo electrónico ya ha sido utilizado para Votar.')

        return cleaned_data
