import unittest

def fizzbuzz_output(number):
    output = ""
    if number % 3 == 0:
        output += "Fizz"
    if number % 5 == 0:
        output += "Buzz"
    if number % 7 == 0:
        output += "Whizz"
    if number % 11 == 0:
        output += "Bang"

    if output == "":
        output = str(number)
    
    return output

class TestFizzBuzz(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(fizzbuzz_output(3), "Fizz")
        self.assertEqual(fizzbuzz_output(6), "Fizz")
        self.assertEqual(fizzbuzz_output(9), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz_output(5), "Buzz")
        self.assertEqual(fizzbuzz_output(10), "Buzz")
        self.assertEqual(fizzbuzz_output(20), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz_output(15), "FizzBuzz")
        self.assertEqual(fizzbuzz_output(30), "FizzBuzz")
        self.assertEqual(fizzbuzz_output(45), "FizzBuzz")

    def test_whizz(self):
        self.assertEqual(fizzbuzz_output(7), "Whizz")
        self.assertEqual(fizzbuzz_output(14), "Whizz")
        self.assertEqual(fizzbuzz_output(21), "FizzWhizz")

    def test_bang(self):
        self.assertEqual(fizzbuzz_output(11), "Bang")
        self.assertEqual(fizzbuzz_output(22), "Bang")
        self.assertEqual(fizzbuzz_output(33), "FizzBang")

    def test_fizzbuzzwhizzbang(self):
        self.assertEqual(fizzbuzz_output(1155), "FizzBuzzWhizzBang")

if __name__ == "__main__":
    unittest.main()
