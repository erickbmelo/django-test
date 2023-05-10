from django import forms
from .models import ResponsavelFamiliar, MembroFamiliar


class ResponsavelFamiliarForm(forms.ModelForm):
    class Meta:
        model = ResponsavelFamiliar
        fields = '__all__'


class MembroFamiliarForm(forms.ModelForm):
    class Meta:
        model = MembroFamiliar
        fields = '__all__'