from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self): ...


    @abstractmethod
    def next(self): ...


