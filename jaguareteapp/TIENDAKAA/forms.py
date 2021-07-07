from django import forms
from .models import Producto

class FormProducto(forms.ModelForm): 

    #campos del modelo
    class Meta:
        model = Producto
        fields = ('categoria', 'titulo', 'descripcion', 'imagen', 'precio')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'pub_titulo'}),
            'descripcion': forms.Textarea(attrs={'class': 'pub_descripcion'}),
            'imagen': forms.FileInput(attrs={'name':'imagen_adjunta', 'class': 'pub_imagen'}),
            'precio': forms.Textarea(attrs={'class': 'pub_precio'}),
        }
