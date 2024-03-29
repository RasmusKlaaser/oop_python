"""Shapes."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """General shape class."""

    def __init__(self, color: str):
        """Shape constructor."""
        self.set_color(color)

    def set_color(self, color: str):
        """Set the color of the shape."""
        self.__color = color

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self.__color

    @abstractmethod
    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        print("Implement area")


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """
        Circle constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The radius value is stored here.
        """

        super().__init__(color)
        self.__radius = radius


    def __repr__(self) -> str:
        """
        Return representation of the circle.

        For this exercise, this should return a string:
        Circle (r: {radius}, color: {color})
        """
        return  f"Circle (r: {self.__radius}, color: {self.get_color()})"


    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Area of the circle is pi * r * r.
        """
        self.__circle_area = float(0)
        self.__circle_area = math.pi * self.__radius * self.__radius
        return self.__circle_area


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """
        Square constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        super().__init__(color)
        self.__side = side


    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f"Square (side: {self.__side}, color: {self.get_color()})"


    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        self.__square_area = float(0)
        self.__square_area = self.__side * self.__side
        return self.__square_area


class Rectangle(Shape):
    def  __init__(self, color: str, length: float, width: float):
        super().__init__(color)
        self.__length = length
        self.__width = width

    def __repr__(self) -> str:
        return f"Rectangle (l: {self.__length}, w: {self.__width}, color: {self.get_color()})"

    def get_area(self) -> float:
        self.__rectangle_area = float(0)
        self.__rectangle_area = self.__length * self.__width
        return self.__rectangle_area

class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Paint constructor."""
        self.__shapes = []

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        self.__shapes.append(shape)

    def get_shapes(self) -> list:
        """Return all the shapes."""
        return self.__shapes

    def calculate_total_area(self) -> float:
        """Calculate total area of the shapes."""
        total_area = 0
        for shape in self.__shapes:
            total_area += float(shape.get_area())
        return total_area

    def get_circles(self) -> list:
        """Return only circles."""
        circles = []
        for shape in self.__shapes:
            if shape.__class__.__name__ == "Circle":
                circles.append(shape)
        return circles

    def get_squares(self) -> list:
        """Return only squares."""
        squares = []
        for shape in self.__shapes:
            if shape.__class__.__name__ == "Square":
                squares.append(shape)
        return squares

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        rectangles = []
        for shape in self.__shapes:
            if shape.__class__.__name__ == "Rectangle":
                rectangles.append(shape)
        return rectangles


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    square = Square("red", 11)
    square = Square("Yellow", 10)
    print(circle)
    print(square)
    paint.add_shape(circle)
    paint.add_shape(square)
    print(paint.calculate_total_area())
    print(paint.get_circles())
    print(paint.get_squares())
    print(paint.get_rectangles())