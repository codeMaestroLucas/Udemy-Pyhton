from abc import ABC, abstractmethod
from vistor import Vistor

class Element(ABC):
    @abstractmethod
    def accept(self, vistor: Vistor) -> None: ...