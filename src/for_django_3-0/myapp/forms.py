from django.forms import ModelForm
from django import forms
from .models import *


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'

        widgets={
            'docfile' : forms.ClearableFileInput()
        }
        
