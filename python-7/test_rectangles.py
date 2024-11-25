import unittest
from rectangles import Point, Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.r = Rectangle(2, 3, 4, 5)
    
    def test_init(self):
        r = Rectangle(2, 3, 4, 5)
        self.assertEqual(r.pt1.x, 2)
        self.assertEqual(r.pt1.y, 3)
        self.assertEqual(r.pt2.x, 4)
        self.assertEqual(r.pt2.y, 5)

    def test_str(self):
        r = Rectangle(2, 3, 4, 5)
        self.assertEqual(str(r), "[(2, 3), (4, 5)]")

    def test_repr(self):
        r = Rectangle(1, 3, 4, 5)
        self.assertEqual(repr(r), "Rectangle(1, 3, 4, 5)")

    def test_eq(self):
        r1 = Rectangle(2, 2, 4, 5)
        r2 = Rectangle(2, 2, 4, 5)
        r3 = Rectangle(3, 4, 5, 6)
        self.assertTrue(r1 == r2)
        self.assertFalse(r1 == r3)

    def test_ne(self):
        r1 = Rectangle(2, 2, 4, 5)
        r2 = Rectangle(2, 2, 4, 5)
        r3 = Rectangle(3, 4, 5, 6)
        self.assertFalse(r1 != r2)
        self.assertTrue(r1 != r3)

    def test_center(self):
        r1 = Rectangle(2, 3, 4, 5)
        r2 = Rectangle(10, 10, 20, 20)
        self.assertEqual(r1.center(), Point(3, 4))
        self.assertEqual(r2.center(), Point(15, 15))

    def test_area(self):
        r1 = Rectangle(2, 3, 4, 5)
        r2 = Rectangle(2, 2, 5, 5)
        self.assertEqual(r1.area(), 4)
        self.assertEqual(r2.area(), 9)

    def test_move(self):
        r1 = Rectangle(3, 2, 4, 5)
        r2 = Rectangle(1, 1, 2, 2)

        self.assertEqual(r1.move(1, 1), Rectangle(4, 3, 5, 6))
        self.assertEqual(r2.move(10, 10), Rectangle(11, 11, 12, 12))

    def test_intersection(self): 
        r1 = Rectangle(2, 3, 4, 5)
        r2 = Rectangle(2, 2, 5, 5)

        self.assertEqual(r1.intersection(r2), Rectangle(2, 3, 4, 5))
        self.assertEqual(r2.intersection(r1), Rectangle(2, 3, 4, 5))

    def test_cover(self):
        r1 = Rectangle(2, 3, 4, 5)
        r2 = Rectangle(2, 2, 5, 5)
        r3 = Rectangle(1, 1, 6, 6)

        self.assertEqual(r1.cover(r2), Rectangle(2, 2, 5, 5))
        self.assertEqual(r2.cover(r1), Rectangle(2, 2, 5, 5))
        self.assertEqual(r1.cover(r3), Rectangle(1, 1, 6, 6))

    def test_make4(self):
        r1 = Rectangle(2, 3, 4, 5)
        r2 = Rectangle(1, 1, 6, 6)
        r3 = Rectangle(0, 0, 7, 7)
        r4 = Rectangle(3, 4, 4, 5)

        self.assertEqual(r1.make4(), [Rectangle(2, 3, 3, 4), Rectangle(3, 3, 4, 4), Rectangle(2, 4, 3, 5), Rectangle(3, 4, 4, 5)])
        self.assertEqual(r2.make4(), [Rectangle(1, 1, 3.5, 3.5), Rectangle(3.5, 1, 6, 3.5), Rectangle(1, 3.5, 3.5, 6), Rectangle(3.5, 3.5, 6, 6)])
        self.assertEqual(r3.make4(), [Rectangle(0, 0, 3.5, 3.5), Rectangle(3.5, 0, 7, 3.5), Rectangle(0, 3.5, 3.5, 7), Rectangle(3.5, 3.5, 7, 7)])
        self.assertEqual(r4.make4(), [Rectangle(3, 4, 3.5, 4.5), Rectangle(3.5, 4, 4, 4.5), Rectangle(3, 4.5, 3.5, 5), Rectangle(3.5, 4.5, 4, 5)])

if __name__ == '__main__':
    unittest.main()


