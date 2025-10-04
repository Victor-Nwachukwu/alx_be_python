import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Create a calculator instance for use in all tests."""
        self.calc = SimpleCalculator()

    # ---------- Addition ----------
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-5, -3), -8)

    def test_addition_mixed_sign_numbers(self):
        self.assertEqual(self.calc.add(-5, 3), -2)

    # ---------- Subtraction ----------
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtraction_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    def test_subtraction_resulting_in_negative(self):
        self.assertEqual(self.calc.subtract(3, 10), -7)

    # ---------- Multiplication ----------
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(6, 7), 42)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(10, 0), 0)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-3, 4), -12)

    # ---------- Division ----------
    def test_division_positive_numbers(self):
        self.assertEqual(self.calc.divide(20, 5), 4)

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(-15, 3), -5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))  # expect None on divide by zero

    def test_division_resulting_in_float(self):
        self.assertEqual(self.calc.divide(7, 2), 3.5)


if __name__ == "__main__":
    unittest.main()
