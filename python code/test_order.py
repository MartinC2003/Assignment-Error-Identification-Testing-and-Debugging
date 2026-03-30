import unittest
from Buggy_Code import Order

class TestOrder(unittest.TestCase):

    # Unit Tests 1
    def test_calculate_total(self):
        order = Order("Test", [("Book", 2, 10.0), ("Pen", 3, 2.0)])
        self.assertEqual(order.calculate_total(), 26.0)

    # Unit Tests 2
    def test_apply_discount(self):
        order = Order("Test", [])
        self.assertEqual(order.apply_discount("SAVE10"), 0.1)
        self.assertEqual(order.apply_discount("SAVE20"), 0.2)
        self.assertEqual(order.apply_discount("INVALID"), 0.0)

    # Integration Test
    def test_order_workflow(self):
        order = Order("Alice", [("Book", 2, 15.0)])
        order.add_item("Notebook", 3, 5.0)
        order.remove_item("Book")
        total = order.calculate_total()

        self.assertEqual(total, 15.0)