import unittest

def multiply(a, b):

   return a * b


class MultiplyTestCase(unittest.TestCase):

   def test_multiply_positive_numbers(self):

       result = multiply(3, 4)

       self.assertEqual(result, 12)


   def test_multiply_negative_numbers(self):

       result = multiply(-2, -5)

       self.assertEqual(result, 10)


   def test_multiply_zero(self):

       result = multiply(10, 0)

       self.assertEqual(result, 0)


   def test_multiply_with_one(self):

       result = multiply(7, 1)

       self.assertEqual(result, 7)