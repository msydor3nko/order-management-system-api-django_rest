from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response

from .serializers import OrderSerializer, InvoiceSerializer
from .models import Order, Invoice


class OrdersList(generics.ListAPIView):
    """List of all orders (accountant)."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrdersListPeriod(generics.ListAPIView):
    """
    List of orders for period (accountant).

    Examples
        :url: `/api/v1/orders/2020-01-01&2020-12-31`
        :start_date: `2020-01-01`
        :end_date: `2020-12-31`
    """

    serializer_class = OrderSerializer

    def get_queryset(self):
        start_date = self.kwargs.get('start_date')
        end_date = self.kwargs.get('end_date')

        return Order.objects.filter(created_at__range=(start_date, end_date))


class OrderCreate(generics.CreateAPIView):
    """Create new order (cashier)."""

    serializer_class = OrderSerializer
    # TODO: validate payload in POST request: should be `Product` and `Order.status` as `Created` only


class OrderReadUpdate(generics.RetrieveUpdateAPIView):
    """Read/Update order status on `Completed` (seller) or `Payed` (cashier)."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # TODO: only order status should be allowed for updating/patching


class InvoiceGenerate(generics.ListCreateAPIView):
    """Generate invoice by order (cashier)."""

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
