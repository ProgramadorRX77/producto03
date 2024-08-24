from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'codigo', 'descripcion', 'precio', 'tipo', 'imagen']

    def validate_precio(self, value):
        if value < 100:
            raise serializers.ValidationError("El precio no puede ser menor a 100 pesos.")
        return value
