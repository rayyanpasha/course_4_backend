"""
# Input - ecpected output - reason
# Test case 1
Helloworld@123 - true - cointains capital letter, not capital letter , special characters , numbers and longer than 8
# Test case 2
helloworld - false - does not contain capital letter
# Test case 3
helloworld123 - false - does not contain special characters
# Test case 4
helloworld@ - false - does not contain numbers
# Test case 5
helloworld123456 - false - no caps
# Test case 6
@1234GGGGGmy - true - contains capital letter, special characters, numbers and 8 characters long
# Test case 7
@MYVertyugfg1234 - true - contains capital letter, special characters, numbers and 8 characters
# Test case 8
helLoworld@123456 - TRUE - contains capital letter, special characters, numbers and 8 characters
# Test case 9
helloworld@123 - true - contains capital letter, special characters, numbers and 8 characters
# Test case 10
habx@K121112 - true - contains capital letter, special characters, numbers"""

# Unit Tests for Calculator App

# Run with the following command:
# python3 -m unittest test_calculator.py
# or just press the Run button on the top right!
import unittest
from password_validator import validate_password  # Import the function directly

class TestPasswordValidation(unittest.TestCase):
    def test_case_1(self):
        result = validate_password("Helloworld@123")  
        self.assertEqual(result, True)

    def test_case_2(self):
        result2 = validate_password("helloworld")
        self.assertEqual(result2, False)

    def test_case_3(self):
        result3 = validate_password("helloworld123")
        self.assertEqual(result3, False)

    def test_case_4(self):
        result4 = validate_password("helloworld@")
        self.assertEqual(result4, False)

    def test_case_5(self):
        result5 = validate_password("helloworld123456")
        self.assertEqual(result5, False)  

    def test_case_6(self):
        result6 = validate_password("@1234GGGGGmy")
        self.assertEqual(result6, True)

    def test_case_7(self):
        result7 = validate_password("@MYVertyugfg1234")
        self.assertEqual(result7, True)

    def test_case_8(self):
        result8 = validate_password("helLoworld@123456")
        self.assertEqual(result8, True)

    def test_case_9(self):
        result9 = validate_password("helLoworld@123")
        self.assertEqual(result9, True)

    def test_case_10(self):
        result10 = validate_password("habx@K121112")
        self.assertEqual(result10, True)

if __name__ == '__main__':
    unittest.main()