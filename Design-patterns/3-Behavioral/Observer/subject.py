from abc import ABC, abstractmethod

from observer import Observer

class Subject(ABC):
    
    @abstractmethod
    def attach(self): ...
    
    @abstractmethod
    def dettach(self): ...
    
    @abstractmethod
    def notify(self): ...


class WeatherStation(Subject):
    def __init__(self) -> None:
        self._observers = []
        self._temperature: float = 0.0
        
    
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)
        print(f'Observer {observer._name} \033[32mattached\033[m.')
    
    
    def dettach(self, observer: Observer) -> None:
        self._observers.remove(observer)
        print(f'Observer {observer._name} \033[31mdettached\033[m.')
    
    
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature)
        
    def set_temperature(self, new_temperature: float) -> None:
        self._temperature = new_temperature
        self.notify()