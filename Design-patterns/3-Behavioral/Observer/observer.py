from abc import ABC, abstractmethod

class Observer(ABC):
    
    @abstractmethod
    def update(self): ...

class DisplayDevice(Observer):
    def __init__(self, name: str) -> None:
        self._name = name

    def update(self, temperature: float) -> None:
        print(f'{self._name} display: Temperature is {temperature}°C')