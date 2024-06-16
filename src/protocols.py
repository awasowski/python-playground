# Protocols introduced in Python 3.8 allow for structural subtyping
# (duck typing) enabling type checking based on the presence of methods
# and properties rather than explicit inheritance.

from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None:
        pass

class Circle:
    def draw(self) -> None:
        print("Drawing a circle")

class Square:
    def draw(self) -> None:
        print("Drawing a square")

def render_shape(shape: Drawable) -> None:
    shape.draw()


circle = Circle()
square = Square()
render_shape(circle)  # Output: Drawing a circle
render_shape(square)  # Output: Drawing a square

# Uncommenting the following lines will result in a mypy error
# class Triangle:
#     def display(self) -> None:
#         print("Displaying a triangle")


# triangle = Triangle()
# # Argument 1 to "render_shape" has incompatible type "Triangle"; expected "Drawable"
# render_shape(triangle)
