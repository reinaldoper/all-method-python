from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Testando as classes


circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Área do círculo:", circle.area())
print("Perímetro do círculo:", circle.perimeter())
print("Área do retângulo:", rectangle.area())
print("Perímetro do retângulo:", rectangle.perimeter())
