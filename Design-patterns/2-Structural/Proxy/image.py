from abc import ABC, abstractmethod

class Image(ABC):
    
    @abstractmethod
    def display(self): ...


class RealImage(Image):
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self._load_from_disk()
        
    def _load_from_disk(self) -> None:
        print(f"Loading {self.filename} \033[31mfrom\033[m disk...")

    def display(self):
        print(f'Displaying {self.filename}')


class ProxyImage(Image):
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.real_image = None
        
    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        
        self.real_image.display()