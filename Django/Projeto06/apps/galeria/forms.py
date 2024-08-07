from django import forms
from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada',]
        labels = {
            'descricao': 'Descrição',
            'data_fotografia': 'Data de registro',
            'usuario': 'Usuario', 
        } 
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form.control'}),
            'legenda': forms.TextInput(attrs={'class':'form.control'}),
            'cadegoria': forms.Select(attrs={'class':'form.control'}),
            'descrição': forms.Textarea(attrs={'class':'form.control'}),
            'foto': forms.FileInput(attrs={'class':'form.control'}),
            'data_fotografia': forms.DateInput(
                format= '%d/%m/%Y', 
                attrs={
                    'type': 'date', 
                    'class':'form.control'
                    }
            ),
             'usuario': forms.Select(attrs={'class':'form.control'}),
        }
