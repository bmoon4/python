class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.x + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


point = Point(10, 20)
other = Point(1, 2)
combined = point + other
print(combined)
