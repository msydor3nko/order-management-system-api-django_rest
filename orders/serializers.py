from rest_framework import serializers

from .models import Order, Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'created_at', 'name', 'price', 'discount_price')


class OrderSerializer(serializers.ModelSerializer):

    product_name = serializers.ReadOnlyField(source='product.name')
    product_price = serializers.ReadOnlyField(source='product.price')
    product_discount_price = serializers.ReadOnlyField(source='product.discount_price')

    class Meta:
        model = Order
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    """
    TODO: think about validations here
    """
    pass
