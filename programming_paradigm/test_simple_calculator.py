import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---------- Addition Tests ----------
    def test_addition(self):
        """Test addition with positive, negative, and zero values."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)

    # ---------- Subtraction Tests ----------
    def test_subtraction(self):
        """Test subtraction with various inputs."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-2, -3), 1)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # ---------- Multiplication Tests ----------
    def test_multiplication(self):
        """Test multiplication with positive, negative, and zero values."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 3), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    # ---------- Division Tests ----------
    def test_division(self):
        """Test division with various inputs, including division by zero."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(6, -3), -2)
        self.assertEqual(self.calc.divide(0, 3), 0)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero

    def test_division_float_result(self):
        """Test that division returns float results when necessary."""
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(1, 4), 0.25)

if __name__ == "__main__":
    unittest.main()
