from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):

    def test_add_nums(self):
        res = calc.add(5,6)
        self.assertEqual(res, 11)
    
    def test_subtract_nums(self):
        res = calc.substract(10, 15)
        self.assertEqual(res, -5)