from django import forms
from .models import Movie
from django.core.exceptions import ValidationError

from ckeditor.widgets import CKEditorWidget

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['name', 'description', 'rating', 'genders', 'company', 'image', 'premiere' ]

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Película'}),
            'description': CKEditorWidget(),
            
         #   'description': forms.Textarea(attrs={"class": 'form-control', 'placeholder':'Sinopsis'}),
            'rating': forms.Select(attrs={'class':'form-control', 'placeholder':'Rating'}),
            'genders': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Géneros'}),
            'company': forms.Select(attrs={'class':'form-control', 'placeholder':'Compañía'}),
            'premiere': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Año Estreno'}),
        }

        labels = {
            'name': "Título",
            'description': "Sinopsis"
        }