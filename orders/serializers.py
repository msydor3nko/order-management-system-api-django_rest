from rest_framework import serializers

from .models import Order, Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'created_at', 'name', 'price',)


class OrderSerializer(serializers.ModelSerializer):
    """
    TODO: add product details info in `product` field
    """
    class Meta:
        model = Order
        fields = ('id', 'created_at', 'status', 'product',)
