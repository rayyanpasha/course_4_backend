# Unit Tests for Calculator App

# Run with the following command:
# python3 -m unittest test_calculator.py
# or just press the Run button on the top right!

import unittest
import calculator

# Unit tests
class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = calculator.add(10, 5)
        self.assertEqual(result, 15)
    def test_subtract(self):
        result = calculator.subtract(10, 5)
        self.assertEqual(result, 5)
    def test_multiply(self):
        result = calculator.multiply(10, 5)
        self.assertEqual(result, 50)
    def test_divide(self):
        result = calculator.divide(10, 5)
        self.assertEqual(result, 2)    
    # Similarly, test the other functions of the Calculator App.
        

# Run the tests
if __name__ == "__main__":
    unittest.main()