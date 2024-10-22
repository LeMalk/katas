import unittest
from fractions import Fraction

class TestFraction(unittest.TestCase):
    def test_initialization(self):
        with self.assertRaises(ValueError):
            Fraction(1, 0)
        f = Fraction(3, 9)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 3)

    def test_addition(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        result = f1.add(f2)
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 4)

    def test_str(self):
        self.assertEqual(str(Fraction(0, 1)), "0")
        self.assertEqual(str(Fraction(1, 1)), "1")
        self.assertEqual(str(Fraction(3, 1)), "3")
        self.assertEqual(str(Fraction(5, 2)), "2 1/2")
        self.assertEqual(str(Fraction(1, 2)), "1/2")

if __name__ == '__main__':
    unittest.main()