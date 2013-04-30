from unittest import TestCase

from roman.calculator import *


class RomanNumeralTest(TestCase):
    def test_one(self):
        one = RomanNumeral('I')
        self.assertEqual(1, one.to_int())

    def test_four(self):
        four = RomanNumeral('IV')
        self.assertEqual(4, four.to_int())

    # def test_fifteen(self):
    #     fifteen = RomanNumeral('XV')
    #     self.assertEqual(15, fifteen.to_int())
