from unittest import TestCase
from unittest.mock import patch

"""
What if, instead of hard coding a return value, we wanted to run a custom sum function instead?
 Our custom function will mock out the undesired long running time.sleep call and only remain with the actual summing functionality we want to test. We can simply define a side_effect in our test.
"""

def mock_sum(a, b):
    # mock sum function without the long running time.sleep
    return a + b

class TestCalculator(TestCase):
    @patch('main.Calculator.sum', side_effect=mock_sum)
    def test_sum(self, sum):
        self.assertEqual(sum(2,3), 5)
        self.assertEqual(sum(7,3), 10)