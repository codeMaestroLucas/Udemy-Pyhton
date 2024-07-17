from abc import ABC, abstractmethod
from color import Color

class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color
        
    @abstractmethod
    def draw(self): ...
    
        
class Square(Shape):
    
    def draw(self) -> str:
        return f'Drawing an {self.color.apply_color()} Square.'

    
class Circle(Shape):

    def draw(self) -> str:
        return f'Drawing a {self.color.apply_color()} Circle.'