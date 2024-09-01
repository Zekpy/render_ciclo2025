from django import forms
from .models import Inscripcion
from cursos.models import Curso

class InscripcionForm(forms.ModelForm):
    cursos = forms.ModelMultipleChoiceField(
        queryset=Curso.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='Cursos'
    )

    class Meta:
        model = Inscripcion
        fields = ['nombre', 'apellido', 'celular', 'email', 'edad', 'cursos']

    def clean(self):
        cleaned_data = super().clean()
        celular = cleaned_data.get('celular')
        email = cleaned_data.get('email')

        if Inscripcion.objects.filter(celular=celular).exists():
            self.add_error('celular', 'Este número de celular ya ha sido utilizado para votar.')

        if Inscripcion.objects.filter(email=email).exists():
            self.add_error('email', 'Este correo electrónico ya ha sido utilizado para votar.')

        return cleaned_data
