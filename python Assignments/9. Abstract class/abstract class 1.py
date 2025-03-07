from abc import ABC, abstractmethod

class Shape(ABC):
    """
    An abstract base class representing a shape.
    """

    def __init__(self, color="unknown"):
        """
        Initializes the shape with a color.
        """
        self.color = color

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        Must be implemented by subclasses.
        """
        pass

    def get_color(self):
        """
        Non-abstract method to get the color of the shape.
        """
        return self.color

    def describe(self):
        """
        Non-abstract method to describe the shape.
        """
        return f"This is a {self.__class__.__name__} with color {self.color}."


class Circle(Shape):
    """
    A concrete class representing a circle, inheriting from Shape.
    """

    def __init__(self, radius, color="blue"):
        """
        Initializes the circle with a radius and color.
        """
        super().__init__(color)
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.
        """
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        """
        Calculates the perimeter (circumference) of the circle.
        """
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    """
    A concrete class representing a rectangle, inheriting from Shape.
    """

    def __init__(self, width, height, color="red"):
        """
        Initializes the rectangle with width, height, and color.
        """
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

# Example usage:

circle = Circle(5)
rectangle = Rectangle(4, 6, "green")

print(circle.describe())
print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")

print(rectangle.describe())
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")

print(f"Circle color: {circle.get_color()}")
