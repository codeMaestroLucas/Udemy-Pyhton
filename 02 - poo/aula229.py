# Abstract Classes: Abstract Base Class - ABC
    # Can't be instancieted, just declareted.

from abc import ABC, abstractmethod

class Log(ABC):
    @abstractmethod
    def _log(self, msg: str): ...

    def log_error(self, msg: str):
        return self._log(f'Error: {msg}')
    
    def log_sucess(self, msg: str):
        return self._log(f'Sucess: {msg}')