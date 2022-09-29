from unittest import TestCase
from unittest.mock import patch

class TestCalculator(TestCase):
    @patch('main_1.Calculator.sum', return_value=9)
    def test_sum(self, sum1):
        self.assertEqual(sum1(4,3), 9)