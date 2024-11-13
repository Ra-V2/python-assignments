import unittest
from points import Point
from rectangles import Rectangle

class TestPoint(unittest.TestCase):
    def setUp(self) -> None:
        self.p = Point(2, 3)
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_init(self):
        p = Point(4, 3)
        self.assertEqual(p.x, 4)
        self.assertEqual(p.y, 3)
    
    def test_str(self):
        p = Point(4, 3)
        self.assertEqual(str(p), "(4, 3)")

    def test_repr(self):
        p = Point(2, 3)
        self.assertEqual(repr(p), "Point(2, 3)")

    def test_eq(self):
        p1 = Point(2, 3)
        p2 = Point(2, 3)
        p3 = Point(3, 4)
        self.assertTrue(p1 == p2)
        self.assertFalse(p1 == p3)

    def test_ne(self):
        p1 = Point(2, 3)
        p2 = Point(2, 3)
        p3 = Point(3, 4)
        self.assertFalse(p1 != p2)
        self.assertTrue(p1 != p3)

    def test_add(self):
        p1 = Point(2, 3)
        p2 = Point(3, 4)
        p3 = Point(0, 0)
        p4 = Point(0, -5)
        self.assertEqual(p1 + p2, (5, 7))
        self.assertEqual(p1 + p3, (2, 3))
        self.assertEqual(p1 + p4, (2, -2))

    def test_sub(self):
        p1 = Point(5, 3)
        p2 = Point(3, 4)
        p3 = Point(0, 0)
        p4 = Point(0, -5)
        self.assertEqual(p1 - p2, (2, -1))
        self.assertEqual(p1 - p3, (5, 3))
        self.assertEqual(p1 - p4, (5, 8))

    def test_mul(self):
        p1 = Point(3, 3)
        self.assertEqual(p1 * 3, (9, 9))

    def test_cross(self):
        p1 = Point(2, 3)
        p2 = Point(3, 4)
        self.assertEqual(p1.cross(p2), -1)
        self.assertEqual(p2.cross(p1), 1)
            
    def test_length(self):
        p1 = Point(3, 4)
        p2 = Point(-2, 5)
        self.assertEqual(p1.length(), 5)
        self.assertAlmostEqual(p2.length(), 5.385164807134504)

    def test_hash(self):
        p1 = Point(5, 3)
        self.assertEqual(hash(p1), hash((5, 3)))

class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.r = Rectangle(2, 3, 4, 5)

    def tearDown(self) -> None:
        return super().tearDown()
    
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
        r2 = Rectangle(5, 5, 2, 2)
        r3 = Rectangle(0, 0, 0, 0)
        self.assertEqual(r1.center(), Point(3, 4))
        self.assertEqual(r2.center(), Point(3.5, 3.5))
        self.assertEqual(r3.center(), Point(0, 0))

    def test_area(self):
        r1 = Rectangle(2, 3, 4, 5)
        r2 = Rectangle(5, 5, 2, 2)
        r3 = Rectangle(2, 2, 2, 2)
        r4 = Rectangle(5, 1, 4, 2)
        self.assertEqual(r1.area(), 4)
        self.assertEqual(r2.area(), 9)
        self.assertEqual(r3.area(), 0)
        self.assertEqual(r4.area(), 1)

    def test_move(self):
        r1 = Rectangle(5, 6, 4, 5)
        r2 = Rectangle(1, 1, 2, 2)
        self.assertEqual(r1.move(1, 1), Rectangle(6, 7, 5, 6))
        self.assertEqual(r2.move(-2, -2), Rectangle(-1, -1, 0, 0))

if __name__ == '__main__':
    unittest.main()


