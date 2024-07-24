from element import Element
from vistor import Vistor


class Circle(Element):
    def __init__(self, radius: float) -> None:
        self.radius = radius
        
    def accept(self, visitor: Vistor) -> None:
        visitor.visit_circle(self)


class Square(Element):
    def __init__(self, side: float) -> None:
        self.side = side
        
    def accept(self, visitor: Vistor) -> None:
        visitor.visit_square(self)


class Rectangle(Element):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
        
    def accept(self, visitor: Vistor) -> None:
        visitor.visit_rectangle(self)