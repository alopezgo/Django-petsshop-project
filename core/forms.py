from django import forms
from django.forms import ModelForm
from .models import Producto, Cliente


class ProductosForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"


class FormularioCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
