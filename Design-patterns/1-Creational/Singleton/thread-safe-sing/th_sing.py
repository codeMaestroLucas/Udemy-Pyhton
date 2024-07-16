from threading import Lock

class Singleton:
    _instance = None
    _lock = Lock()
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value: str) -> None:
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True
            
    def __repr__(self) -> str:
        return f'ThreadSafeSingleton {self.value}.'