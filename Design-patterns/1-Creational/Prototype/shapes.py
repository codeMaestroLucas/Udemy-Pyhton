from abc import ABC, abstractmethod
from prototype import Prototype

class Shape(Prototype, ABC):
    """Abstract class
    """
    @abstractmethod
    def __init__(self, shape: str):
        self._shape = shape
    
    @abstractmethod
    def __repr__(self):
        return f'Shape({self._shape})'


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__('Rectangle')
        self.width = width
        self.height = height
    
    def __repr__(self):
        return f'Rectangle {self.width}X{self.height}cm.\n\
Space: {self.width * self.height:.1f}cm²'


class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__('Circle')
        self.radius = radius

    def __repr__(self):
        return f'Circle with radius {self.radius}cm.\n\
Space: {3.14 * self.radius ** 2:.1f}cm²'