import unittest
from lesson_12 import homework_12_3

class test_pages_amount(unittest.TestCase):
    def test_valid_number(self):
        self.assertEqual(1, homework_12_3.calculate_page_amount(8))
        self.assertEqual(2, homework_12_3.calculate_page_amount(9))
        self.assertEqual(1, homework_12_3.calculate_page_amount(1))

    def test_negative(self):
        self.assertEqual(0, homework_12_3.calculate_page_amount(0))
        self.assertEqual(0, homework_12_3.calculate_page_amount(-1))

    def test_invalid_numeric(self):
        with self.assertRaises(TypeError):
            homework_12_3.calculate_page_amount(4.26)
        with self.assertRaises(TypeError):
            homework_12_3.calculate_page_amount(True)
        with self.assertRaises(TypeError):
            homework_12_3.calculate_page_amount('text')

if __name__ == '__main__':
    unittest.main()