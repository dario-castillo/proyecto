from django import forms

class BuscaCursoForm(forms.Form):
    nombre = forms.CharField()
