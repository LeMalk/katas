import unittest
from closest_to_zero import closest_to_zero

class TestClosestToZero(unittest.TestCase):
    
    def test_positive_numbers(self):
        self.assertEqual(closest_to_zero([1, 2, 3, 4, 5]), 1)
    
    def test_negative_numbers(self):
        self.assertEqual(closest_to_zero([-1, -2, -3, -4, -5]), -1)
    
    def test_mixed_numbers(self):
        self.assertEqual(closest_to_zero([6, -9, 15, -2, 2, 11]), 2)
    
    def test_empty_list(self):
        self.assertIsNone(closest_to_zero([]))
    
    def test_single_element(self):
        self.assertEqual(closest_to_zero([10]), 10)
    
    def test_zero_in_list(self):
        self.assertEqual(closest_to_zero([0, 1, -1, 2, -2]), 0)
    
    def test_equal_distance(self):
        self.assertEqual(closest_to_zero([-2, 2]), 2)
        self.assertEqual(closest_to_zero([-3, 3]), 3)
    
    def test_all_zeros(self):
        self.assertEqual(closest_to_zero([0, 0, 0]), 0)

if __name__ == '__main__':
    unittest.main()