import pytest
from rectangles import Point, Rectangle

class TestRectangle():
    def setup_method(self):
        self.r = Rectangle(2, 3, 4, 5)

    def test_init(self):
        r = Rectangle(2, 3, 4, 5)
        assert r.pt1.x == 2
        assert r.pt1.y == 3
        assert r.pt2.x == 4
        assert r.pt2.y == 5

    def test_invalid_init(self):
        with pytest.raises(ValueError):
            Rectangle(5, 3, 1, 5)

    def test_str(self):
        r = Rectangle(2, 3, 4, 5)
        assert str(r) == "[(2, 3), (4, 5)]"

    def test_repr(self):
        r = Rectangle(1, 3, 4, 5)
        assert repr(r) == "Rectangle(1, 3, 4, 5)"

    def test_eq(self):
        r1 = Rectangle(2, 2, 4, 5)
        r2 = Rectangle(2, 2, 4, 5)
        r3 = Rectangle(3, 4, 5, 6)
        assert r1 == r2
        assert r1 != r3

    def test_ne(self):
        r1 = Rectangle(2, 2, 4, 5)
        r2 = Rectangle(2, 2, 4, 5)
        r3 = Rectangle(3, 4, 5, 6)
        assert r1 == r2
        assert r1 != r3

    def test_center(self):
        r1 = Rectangle(2, 3, 4, 5)
        r2 = Rectangle(10, 10, 20, 20)
        assert r1.center == Point(3, 4)
        assert r2.center == Point(15, 15)

    def test_area(self):
        r1 = Rectangle(2, 3, 4, 5)
        r2 = Rectangle(2, 2, 5, 5)
        assert r1.area() == 4
        assert r2.area() == 9

    def test_move(self):
        r1 = Rectangle(3, 2, 4, 5)
        r2 = Rectangle(1, 1, 2, 2)

        assert r1.move(1, 1) == Rectangle(4, 3, 5, 6)
        assert r2.move(10, 10) == Rectangle(11, 11, 12, 12)

    def test_intersection(self):
        r1 = Rectangle(2, 3, 4, 5)
        r2 = Rectangle(2, 2, 5, 5)

        assert r1.intersection(r2) == Rectangle(2, 3, 4, 5)
        assert r2.intersection(r1) == Rectangle(2, 3, 4, 5)
    
    def test_cover(self):
        r1 = Rectangle(2, 3, 4, 5)
        r2 = Rectangle(2, 2, 5, 5)
        assert r1.cover(r2) == Rectangle(2, 2, 5, 5)
        assert r2.cover(r1) == Rectangle(2, 2, 5, 5)
    
    def test_make4(self):
        r = Rectangle(2, 3, 4, 5)
        r1 = Rectangle(2, 3, 3, 4)
        r2 = Rectangle(3, 3, 4, 4)
        r3 = Rectangle(2, 4, 3, 5)
        r4 = Rectangle(3, 4, 4, 5)
        assert r.make4() == [r1, r2, r3, r4]

    def test_from_points(self):
        pt1 = Point(2, 3)
        pt2 = Point(4, 5)
        r = Rectangle.from_points([pt1, pt2])
        assert r == Rectangle(2, 3, 4, 5)

    def test_invalid_from_points(self):
        pt1 = Point(2, 3)
        with pytest.raises(ValueError):
            Rectangle.from_points([pt1])

    def test_properties(self):
        r = Rectangle(2, 3, 4, 5)
        assert r.top == 5
        assert r.bottom == 3
        assert r.left == 2
        assert r.right == 4
        assert r.width == 2
        assert r.height == 2
        assert r.topleft == Point(2, 5)
        assert r.bottomright == Point(4, 3)
        assert r.topright == Point(4, 5)
        assert r.bottomleft == Point(2, 3)
        assert r.center == Point(3, 4)

    def test_zero_area(self):
        with pytest.raises(ValueError):
            Rectangle(2, 3, 2, 3)
        
    def test_move_negative(self):
        r = Rectangle(2, 3, 4, 5)
        moved_r = r.move(-1, -1)
        assert moved_r == Rectangle(1, 2, 3, 4)

    def test_intersection_no_overlap(self):
        r1 = Rectangle(2, 3, 4, 5)
        r2 = Rectangle(5, 6, 7, 8)
        
        with pytest.raises(ValueError):
            r1.intersection(r2)

    def test_cover_no_overlap(self):
        r1 = Rectangle(2, 3, 4, 5)
        r2 = Rectangle(5, 6, 7, 8)
        assert r1.cover(r2) == Rectangle(2, 3, 7, 8)


# Run the tests
if __name__ == '__main__':
    pytest.main()

