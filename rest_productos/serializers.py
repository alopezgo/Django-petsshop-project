from rest_framework import serializers
from core.models import Producto, Mascota


class ProductoSerializer(serializers.ModelSerializer):

    desc_categoria = serializers.CharField(source="categoria")

    class Meta:
        model = Producto
        fields = ['idproducto', 'marca',
                  'desc_categoria', 'descripcion', 'imagen']


class MascotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mascota
        fields = ['idMascota', 'nombreMascota',
                  'edadAnioMascota', 'edadMesesMascota', 'sexoMascota', 'estEstirizadoMascota', 'razaMascota', 'fotoMascota']
