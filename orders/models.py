from django.db import models

from orders.services.discount import calculate_discount_price


class Product(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    @property
    def discount_price(self):
        return calculate_discount_price(self.price, self.created_at)

    def __str__(self):
        return self.name


class Order(models.Model):

    class StatusType(models.TextChoices):
        CREATED = 'Created'
        COMPLETED = 'Completed'
        PAYED = 'Payed'

    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    status = models.CharField(
        max_length=10,
        choices=StatusType.choices,
        default=StatusType.CREATED
    )

    def __str__(self):
        return f'{self.pk} — {self.product.name}'


# class Invoice(models.Model):
#     product_name = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
#     product_price = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
#     order_created_at = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.pk} — {self.product_name}'
