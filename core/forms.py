from django import forms
from django.forms import ModelForm
from .models import Producto

class ProductosForm(ModelForm):
    
    class Meta:
        model = Producto
        fields = ['idproducto', 'marca', 'categoria', 'descripcion', 'imagen']