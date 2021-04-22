from rest_framework import serializers

from .models import Order, Invoice


class OrderSerializer(serializers.ModelSerializer):

    product_name = serializers.ReadOnlyField(source='product.name')
    product_price = serializers.ReadOnlyField(source='product.price')
    product_discount_price = serializers.ReadOnlyField(source='product.discount_price')

    class Meta:
        model = Order
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = ('order', 'order_date', 'product_name', 'product_price', 'product_discount_price', 'created_at')
