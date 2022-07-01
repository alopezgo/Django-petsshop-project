from rest_framework import serializers
from core.models import Producto, Mascota


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ['idproducto', 'marca',
                  'categoria', 'descripcion', 'imagen']


class MascotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mascota
        fields = ['idMascota', 'nombreMascota',
                  'edadAnioMascota', 'edadMesesMascota', 'sexoMascota', 'estEstirizadoMascota', 'razaMascota', 'fotoMascota']
