from rest_framework import serializers
from .models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Products'
        fields = ['id', 'name', 'description', 'price', 'created_at', 'updated_at']
