from contatos.models import Contato
from django import forms


class FormContato(forms.ModelForm):
    
    class Meta:
        model = Contato
        fields = "__all__"
        exclude = ('data_criacao', )
