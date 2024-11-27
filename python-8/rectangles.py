from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Invalid rectangle coordinates")
        
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    @classmethod
    def from_points(cls, points):
        if len(points) != 2:
            raise ValueError("Invalid number of points")

        
        pt1, pt2 = points
        return cls(pt1.x, pt1.y, pt2.x, pt2.y)

    @property
    def top(self):
        return self.pt2.y

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        return abs(self.pt2.x - self.pt1.x)

    @property
    def height(self):
        return abs(self.pt2.y - self.pt1.y)

    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)

    @property
    def topright(self):
        return self.pt2

    @property
    def bottomleft(self):
        return self.pt1
        
    @property
    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)
    
    def __str__(self):
        return "[{0}, {1}]".format(self.pt1, self.pt2)

    def __repr__(self):
        return "Rectangle({0}, {1}, {2}, {3})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def area(self):
        return abs((self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y))
        
    def move(self, x, y):
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)
    
    def intersection(self, other):
        return Rectangle(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y), min(self.pt2.x, other.pt2.x), min(self.pt2.y, other.pt2.y))

    def cover(self, other):
        return Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y), max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))

    def make4(self):
        center = self.center
        return [Rectangle(self.pt1.x, self.pt1.y, center.x, center.y), Rectangle(center.x, self.pt1.y, self.pt2.x, center.y), Rectangle(self.pt1.x, center.y, center.x, self.pt2.y), Rectangle(center.x, center.y, self.pt2.x, self.pt2.y)]
    

