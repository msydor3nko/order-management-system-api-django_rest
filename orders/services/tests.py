from datetime import datetime, timedelta
from decimal import Decimal
import unittest

from orders.services.discount import calculate_discount_price


class DiscountTest(unittest.TestCase):

    def test_calculate_discount_price(self):
        """
        Test for calculation for `calculate_discount_price()` function.
        """
        actual_result = calculate_discount_price(
            product_price=101,
            product_date=datetime.now()-timedelta(days=32)
        )
        self.assertEqual(actual_result, Decimal('80.80'))


if __name__ == "__main__":
    unittest.main()
