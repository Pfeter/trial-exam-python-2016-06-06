import unittest
from exam4 import greeter

class TestAnagrammAndCountLetters(unittest.TestCase):

    def test_working_name_correct_result(self):
        result = greeter('Peter')
        self.assertEqual('Hello, Peter!', result)

    def test_empty_name_correct_result(self):
        result = greeter('')
        self.assertEqual('Hello, Mr Nobody!', result)

if __name__ == '__main__':
    unittest.main()
