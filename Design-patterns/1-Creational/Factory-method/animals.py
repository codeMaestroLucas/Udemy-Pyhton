from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract class that is used to define the common Attr and Methods of the
    subclasses.
    """
    def __init__(self, name: str, breed: str) -> None:
        self._name = name.title().strip()
        self._breed = breed

    @abstractmethod
    def say_hi(self) -> str:
        pass
        
    def __repr__(self) -> str:
        return f"{self._name} is an {self._breed}."
  
    
class Dog(Animal):
    """Dog class that will be instantieted.

    Args:
        Animal (ABC): Abstract class Animal.
    """
    def __init__(self, name: str) -> None:
        super().__init__(name, "Dog")
        
    def say_hi(self) -> None:
        return f"{self._name}'s says Woof Woof!"


class Cat(Animal):
    """Cat class that will be instantieted.

    Args:
        Animal (ABC): Abstract class Animal.
    """
    def __init__(self, name: str) -> None:
        super().__init__(name, "Cat")
        
    def say_hi(self) -> None:
        return f"{self._name}'s says Meow!"