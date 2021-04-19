from rest_framework import generics
from rest_framework import views

from .models import Order, Product
from .serializers import OrderSerializer, ProductSerializer


class OrderList(generics.ListAPIView):
    """Provides order listing by period for accountant."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreate(generics.CreateAPIView):
    """Provides order creating for cashier."""
    pass


class OrderUpdate(generics.UpdateAPIView):
    """
    Provides order status updating:
    - completing (for seller)
    - paying (for cashier)
    """
    pass


class InvoiceGenerate(views.APIView):
    """Provides invoice generating for cashier."""
    pass