from django import forms

class FormGenre(forms.Form):
    name = forms.CharField(max_length=20, label='Gênero')
    