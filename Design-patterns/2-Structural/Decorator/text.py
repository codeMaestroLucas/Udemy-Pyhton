from abc import ABC, abstractmethod

class Text(ABC):
    @abstractmethod
    def render(self) -> str: ...

class SimpleText(Text):
    def __init__(self, text: str) -> None:
        self.text = text
        
    def render(self) -> str:
        return self.text