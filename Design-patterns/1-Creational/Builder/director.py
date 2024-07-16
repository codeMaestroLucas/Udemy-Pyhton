from builders import HouseBuilder
from house import House


class Director:
    """Class used to instantiate the Builder.
    The house will be build with the specific characteristics by the builder.
    """
    def __init__(self, builder: HouseBuilder):
        """Defines the specific builder
        (WoodenHouseBuilder | ConcreteHouseBuilder).
        """
        self.builder = builder
        
    def build_house(self,
                    foundation: str = None,
                    structure: str = None,
                    roof: str = None,
                    interior: str = None,
                    rooms: int = None) -> House:
        """Function used to build an House

        Returns:
            House: House instatiated with the characteristics specified.
        """
        
        self.builder.set_foundation(foundation)
        self.builder.set_structure(structure)
        self.builder.set_roof(roof)
        self.builder.set_interior(interior)
        self.builder.set_rooms(rooms)
        
        return self.builder.get_house()