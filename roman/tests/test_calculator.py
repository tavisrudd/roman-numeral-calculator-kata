from unittest import TestCase

from roman.calculator import *


class RomanNumeralTest(TestCase):
    def test_one(self):
        one = RomanNumeral('I')
        self.assertEqual(1, one.value)

    def test_four(self):
        four = RomanNumeral('IV')
        self.assertEqual(4, four.value)

    def test_fifteen(self):
        fifteen = RomanNumeral('XV')
        self.assertEqual(15, fifteen.value)

    def test_fourteen(self):
        fourteen = RomanNumeral('XIV')
        self.assertEqual(14, fourteen.value)

    def test_hundred_and_nine(self):
        self.assertEqual(109, RomanNumeral('CIX').value)

    def test_add_them(self):
        res = RomanNumeral('X') + RomanNumeral('V')
        self.assertEqual(15, res.value)

