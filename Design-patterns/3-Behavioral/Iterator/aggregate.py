from abc import ABC, abstractmethod

class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self): ...


