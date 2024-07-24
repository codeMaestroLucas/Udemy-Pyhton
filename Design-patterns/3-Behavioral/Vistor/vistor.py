from abc import ABC, abstractmethod

class Vistor(ABC):
    
    @abstractmethod
    def visit_circle(self, circle) -> None: ...
    
    @abstractmethod
    def visit_square(self, square) -> None: ...
    
    @abstractmethod
    def visit_rectangle(self, rectangle) -> None: ...
    
    
class AreaVistor(Vistor):

    def visit_circle(self, circle) -> None:
        area: float = 3.14 * circle.radius ** 2
        print(f'The area of the \033[31mcircle\033[m is: {area:.2f} U.C.')

    def visit_square(self, square) -> None:
        area: float = square.side ** 2
        print(f'The area of the \033[32msquare\033[m is: {area:.2f} U.C.')

    def visit_rectangle(self, rectangle) -> None:
        area: float = rectangle.height * rectangle.width
        print(f'The area of the \033[33mrectangle\033[m is: {area:.2f} U.C.')