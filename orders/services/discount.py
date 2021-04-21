import calendar
from datetime import date, timedelta
from decimal import Decimal


def calculate_discount_price(product_price, product_date):
    """
    Calculating a 20%-discount price if product was added more than 1 month ago.
    """
    discount_start_date = product_date.date() + timedelta(
        days=calendar.monthrange(product_date.year, product_date.month)[1]
    )
    if date.today() >= discount_start_date:
        discount_price = product_price * Decimal('0.8')
        return discount_price.quantize(Decimal('1.00'))

    return product_price
