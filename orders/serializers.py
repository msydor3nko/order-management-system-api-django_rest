from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):

    product_name = serializers.ReadOnlyField(source='product.name')
    product_price = serializers.ReadOnlyField(source='product.price')
    product_discount_price = serializers.ReadOnlyField(source='product.discount_price')

    class Meta:
        model = Order
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):

    order = OrderSerializer()
    # order_date = None
    # created_at = None

    class Meta:
        fields = '__all__'
        # fields = ('product_name', 'product_price', 'product_discount_price', 'order_date', 'created_at')
