from django.db import models


class Order(models.Model):

    class OrderStatusChoices(models.TextChoices):
        CREATED = 'Created'
        COMPLETED = 'Completed'
        PAYED = 'Payed'

    created_at = models.DateTimeField(auto_now_add=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.CREATED
    )

    def __str__(self):
        return self.product.name


class Product(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name
