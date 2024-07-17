from abc import ABC, abstractmethod
from house import House

class HouseBuilder(ABC):
    def __init__(self):
        self.house = House()
    
    @abstractmethod
    def set_foundation(self, foundation: str):
        pass

    @abstractmethod
    def set_structure(self, structure: str):
        pass

    @abstractmethod
    def set_roof(self, roof: str):
        pass

    @abstractmethod
    def set_interior(self, interior: str):
        pass

    @abstractmethod
    def set_rooms(self, rooms: int):
        pass


    def get_house(self) -> House:
        return self.house
    

class ConcreteHouseBuilder(HouseBuilder):
    """Builder of an Concrete House.
    """
    def set_foundation(self, foundation: str):
        self.house.foundation = foundation
        
    def set_structure(self, structure: str):
        self.house.structure = structure
        
    def set_roof(self, roof: str):
        self.house.roof = roof
        
    def set_interior(self, interior: str):
        self.house.interior = interior
        
    def set_rooms(self, rooms: int):
        self.house.rooms = rooms
        
    

class WoddenHouseBuilder(HouseBuilder):
    """Builder of an Wodden House.
    """
    def set_foundation(self, foundation: str):
        self.house.foundation = foundation
        
    def set_structure(self, structure: str):
        self.house.structure = structure
        
    def set_roof(self, roof: str):
        self.house.roof = roof
        
    def set_interior(self, interior: str):
        self.house.interior = interior
        
    def set_rooms(self, rooms: int):
        self.house.rooms = rooms