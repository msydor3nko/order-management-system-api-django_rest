from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response

from .serializers import OrderSerializer, ProductSerializer
from .models import Order, Product


class OrdersList(generics.ListAPIView):
    """
    Provides list of all orders (for accountant).
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrdersListPeriod(generics.ListAPIView):
    """
    Provides order listing for period (for accountant).
    """
    serializer_class = OrderSerializer

    def get_queryset(self):
        start_date = self.kwargs.get('start_date')
        end_date = self.kwargs.get('end_date')

        return Order.objects.filter(created_at__range=(start_date, end_date))


class OrderCreate(generics.CreateAPIView):
    """
    Provides order creating for cashier.
    TODO: fix `405 Method Not Allowed` and order status must be `Created` only
    """
    serializer_class = OrderSerializer


class OrderReadUpdate(generics.RetrieveUpdateAPIView):
    """
    Provides reading/updating single order status using `pk` (order `id`):
    - completing (for seller)
    - paying (for cashier)
    TODO: only order status should be allowed for updating/patching
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class InvoiceGenerate(views.APIView):
    """
    Provides order invoice generating for cashier.
    """
    pass
