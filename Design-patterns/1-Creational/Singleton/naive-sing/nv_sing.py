class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value: str) -> None:
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True

    def __repr__(self) -> str:
        return f'NaiveSingleton {self.value}.'