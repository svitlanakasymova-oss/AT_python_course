import unittest
from lesson_12 import homework_12_2

class test_string_reverse(unittest.TestCase):
    def test_valid_string(self):
        self.assertEqual("analtivS", homework_12_2.reverse_string("Svitlana"))

    def test_empty_string(self):
        self.assertEqual("", homework_12_2.reverse_string(""))

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            homework_12_2.reverse_string(1)
        with self.assertRaises(TypeError):
            homework_12_2.reverse_string(True)

if __name__ == "__main__":
    unittest.main()