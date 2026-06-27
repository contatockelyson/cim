from django import forms

from apps.galeria.models import Fotografia


class FotografiaForms(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk and self.instance.data_fotografia:
            self.fields['data_fotografia'].initial = (
                self.instance.data_fotografia.strftime('%Y-%m-%d')
            )

    class Meta:
        model = Fotografia
        exclude = ['publicada']

        labels = {
            'descricao': 'Descrição',
            'data_fotografia': 'Data de registro',
            'usuario': 'Usuário',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),

            'data_fotografia': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }