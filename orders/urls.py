from django.urls import path, re_path

from .views import (
    OrdersList, OrdersListPeriod, OrderCreate, OrderReadUpdate, InvoiceGenerate
)


urlpatterns = [
    path('orders/new/', OrderCreate.as_view(), name='order_create'),
    path('orders/<str:pk>/', OrderReadUpdate.as_view(), name='order_read-update'),

    path('orders/', OrdersList.as_view(), name='orders_list'),
    re_path('orders/(?P<start_date>\d{4}-\d{2}-\d{2})&(?P<end_date>\d{4}-\d{2}-\d{2})$',
            OrdersListPeriod.as_view(), name='orders_list'),

    path('invoice/', InvoiceGenerate.as_view(), name='invoice_generate'),
]


# TODO: convert `start_date` and `end_date` from strings into `datetime`
