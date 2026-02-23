import unittest
from lesson_12 import homework_12_1

class test_Rhombus(unittest.TestCase):
    def setUp(self):
        self.romb = homework_12_1.Rhombus()

    def test_valid_side_a(self):
        setattr(self.romb, "side_a", 12)
        self.assertEqual(12, self.romb.side_a)

    def test_zero_side_a(self):
        setattr(self.romb, "side_a", 0)
        self.assertEqual(0, self.romb.side_a)

    def test_invalid_number_side_a(self):
        setattr(self.romb, "side_a", -1)
        self.assertNotHasAttr(self.romb, "side_a")
        setattr(self.romb, "side_a", 'str')
        self.assertNotHasAttr(self.romb, "side_a")
        setattr(self.romb, "side_a", True)
        self.assertNotHasAttr(self.romb, "side_a")

    def test_valid_angle_a(self):
        setattr(self.romb, "angle_a", 12)
        self.assertEqual(12, self.romb.angle_a)

    def test_invalid_angle_a(self):
        setattr(self.romb, "angle_a", 0)
        self.assertNotHasAttr(self.romb, "angle_a")
        setattr(self.romb, "angle_a", 180)
        self.assertNotHasAttr(self.romb, "angle_a")
        setattr(self.romb, "angle_a", 'str')
        self.assertNotHasAttr(self.romb, "angle_a")
        setattr(self.romb, "angle_a", True)
        self.assertNotHasAttr(self.romb, "angle_a")

    def test_valid_angle_b(self):
        setattr(self.romb, "angle_b", 10)
        self.assertEqual(10, self.romb.angle_b)

    def test_invalid_angle_b(self):
        setattr(self.romb, "angle_b", 0)
        self.assertNotHasAttr(self.romb, "angle_b")
        setattr(self.romb, "angle_b", 180)
        self.assertNotHasAttr(self.romb, "angle_b")
        setattr(self.romb, "angle_b", 'str')
        self.assertNotHasAttr(self.romb, "angle_b")
        setattr(self.romb, "angle_b", True)
        self.assertNotHasAttr(self.romb, "angle_b")

    if __name__ == "__main__":
        unittest.main()