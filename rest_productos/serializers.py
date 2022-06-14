from rest_framework import serializers
from core.models import Producto


class ProductoSerializer(serializers.ModelSerializer):

    desc_categoria = serializers.CharField(source="categoria")

    class Meta:
        model = Producto
        fields = ['idproducto', 'marca',
                  'desc_categoria', 'descripcion', 'imagen']
