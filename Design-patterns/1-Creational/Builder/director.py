from builders import HouseBuilder


class Director:
    def __init__(self, builder: HouseBuilder):
        self.builder = builder
        
    def build_house(self,
                    foundation: str = None,
                    structure: str = None,
                    roof: str = None,
                    interior: str = None,
                    rooms: int = None):
        
        self.builder.set_foundation(foundation)
        self.builder.set_structure(structure)
        self.builder.set_roof(roof)
        self.builder.set_interior(interior)
        self.builder.set_rooms(rooms)
        
        return self.builder.get_house()