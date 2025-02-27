from django import forms
from .models import Tables

class TablesForm(forms.ModelForm):
    class Meta:
        model = Tables
        fields = '__all__'