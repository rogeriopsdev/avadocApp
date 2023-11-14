from django import forms
from django.db.models import fields
from .models import Docente,Discente,Diario,Campi, Curso, Componente, Nivel, Avadoc


class DocenteForm(forms.ModelForm):
    class Meta:
        model=Docente
        fields ='__all__'


class DiscenteForm(forms.ModelForm):
    class Meta:
        model= Discente
        fields='__all__'


class DiarioForm(forms.ModelForm):
    class Meta:
        model= Diario
        fields='__all__'


class CampiForm(forms.ModelForm):
    class Meta:
        model= Campi
        fields ='__all__'


class CursoForm(forms.ModelForm):
    class Meta:
        model= Curso
        fields ='__all__'


class NivelForm(forms.ModelForm):
    class Meta:
        model=Nivel
        fields ='__all__'


class ComponenteForm(forms.ModelForm):
    class Meta:
        model=Componente
        fields= '__all__'


class AvadocForm(forms.ModelForm):
    class Meta:
        model=Avadoc
        fields= '__all__'


