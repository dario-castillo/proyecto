from django import forms

class BuscaCursoForm(forms.Form):
    curso = forms.CharField()
