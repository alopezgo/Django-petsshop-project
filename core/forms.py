from django import forms
from django.forms import ModelForm
from .models import Producto, Cliente


class ProductosForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['idproducto', 'marca', 'categoria', 'descripcion', 'imagen']


class FormularioCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
