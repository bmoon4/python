from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("I'm a circle")


class Triangle(Shape):
    def draw(self):
        print("I'm a triangle")


c = Circle()
t = Triangle()


c.draw()
t.draw()
