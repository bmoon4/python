class Point:
    default_colour = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_colour = "green"

p1 = Point(10, 20)
print(p1.default_colour)
print(Point.default_colour)
p1.draw()


p2 = Point(30, 40)
p2.draw()
