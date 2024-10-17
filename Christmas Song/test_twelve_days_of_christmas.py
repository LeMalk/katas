import unittest
from io import StringIO
import sys
from twelve_days_of_christmas import twelve_days_of_christmas

class TestTwelveDaysOfChristmas(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture print statements
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Reset redirect.
        sys.stdout = sys.__stdout__

    def test_twelve_days_of_christmas(self):
        twelve_days_of_christmas()
        output = self.held_output.getvalue()

        expected_output = (
            "On the first day of Christmas\n"
            "My true love sent to me:\n"
            "A partridge in a pear tree.\n\n"
            "On the second day of Christmas\n"
            "My true love sent to me:\n"
            "Two turtle doves and\n"
            "And A partridge in a pear tree.\n\n"
            "On the third day of Christmas\n"
            "My true love sent to me:\n"
            "Three french hens\n"
            "Two turtle doves and\n"
            "And A partridge in a pear tree.\n\n"
            "On the fourth day of Christmas\n"
            "My true love sent to me:\n"
            "Four calling birds\n"
            "Three french hens\n"
            "Two turtle doves and\n"
            "And A partridge in a pear tree.\n\n"
            "On the fifth day of Christmas\n"
            "My true love sent to me:\n"
            "Five golden rings\n"
            "Four calling birds\n"
            "Three french hens\n"
            "Two turtle doves and\n"
            "And A partridge in a pear tree.\n\n"
            "On the sixth day of Christmas\n"
            "My true love sent to me:\n"
            "Six geese a-laying\n"
            "Five golden rings\n"
            "Four calling birds\n"
            "Three french hens\n"
            "Two turtle doves and\n"
            "And A partridge in a pear tree.\n\n"
            "On the seventh day of Christmas\n"
            "My true love sent to me:\n"
            "Seven swans a-swimming\n"
            "Six geese a-laying\n"
            "Five golden rings\n"
            "Four calling birds\n"
            "Three french hens\n"
            "Two turtle doves and\n"
            "And A partridge in a pear tree.\n\n"
            "On the eighth day of Christmas\n"
            "My true love sent to me:\n"
            "Eight maids a-milking\n"
            "Seven swans a-swimming\n"
            "Six geese a-laying\n"
            "Five golden rings\n"
            "Four calling birds\n"
            "Three french hens\n"
            "Two turtle doves and\n"
            "And A partridge in a pear tree.\n\n"
            "On the ninth day of Christmas\n"
            "My true love sent to me:\n"
            "Nine ladies dancing\n"
            "Eight maids a-milking\n"
            "Seven swans a-swimming\n"
            "Six geese a-laying\n"
            "Five golden rings\n"
            "Four calling birds\n"
            "Three french hens\n"
            "Two turtle doves and\n"
            "And A partridge in a pear tree.\n\n"
            "On the tenth day of Christmas\n"
            "My true love sent to me:\n"
            "Ten lords a-leaping\n"
            "Nine ladies dancing\n"
            "Eight maids a-milking\n"
            "Seven swans a-swimming\n"
            "Six geese a-laying\n"
            "Five golden rings\n"
            "Four calling birds\n"
            "Three french hens\n"
            "Two turtle doves and\n"
            "And A partridge in a pear tree.\n\n"
            "On the eleventh day of Christmas\n"
            "My true love sent to me:\n"
            "Eleven pipers piping\n"
            "Ten lords a-leaping\n"
            "Nine ladies dancing\n"
            "Eight maids a-milking\n"
            "Seven swans a-swimming\n"
            "Six geese a-laying\n"
            "Five golden rings\n"
            "Four calling birds\n"
            "Three french hens\n"
            "Two turtle doves and\n"
            "And A partridge in a pear tree.\n\n"
            "On the twelfth day of Christmas\n"
            "My true love sent to me:\n"
            "Twelve drummers drumming\n"
            "Eleven pipers piping\n"
            "Ten lords a-leaping\n"
            "Nine ladies dancing\n"
            "Eight maids a-milking\n"
            "Seven swans a-swimming\n"
            "Six geese a-laying\n"
            "Five golden rings\n"
            "Four calling birds\n"
            "Three french hens\n"
            "Two turtle doves and\n"
            "And A partridge in a pear tree.\n\n"
        )

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()