from builders import ConcreteHouseBuilder, WoddenHouseBuilder
from director import Director


def main() -> None:
    """Function used to run the main code."""
    
    concrete_house_builder = ConcreteHouseBuilder()
    director = Director(concrete_house_builder)
    concrete_house = director.build_house("Concrete",
                                          "Brick",
                                          rooms= 5)
    print(concrete_house)


    wooden_house_builder = WoddenHouseBuilder()
    director = Director(wooden_house_builder)
    wooden_house = director.build_house("Wood",
                                        "Wood",
                                        "Shingles",
                                        "Rustic",
                                        2)
    print(wooden_house)
    
    x_house = director.build_house(foundation= 'Concrete',
                                   roof= 'Stone',
                                   interior= 'Ugly',
                                   rooms= 1)

    print(x_house)
if __name__ == '__main__':
    main()