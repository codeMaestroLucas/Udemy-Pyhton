from abc import ABC, abstractmethod

class Color(ABC):
    
    @abstractmethod
    def apply_color(self): ...
        
class Red(Color):
    def apply_color(self) -> str:
        return '\033[31mred\033[m'
        
class Blue(Color):
    def apply_color(self) -> str:
        return '\033[34mblue\033[m'