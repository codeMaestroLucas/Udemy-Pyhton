# DATACLASSES

from dataclasses import dataclass, field

@dataclass() # U can add another values in this decorator to change the operating
# mode of the class.
class Person:
    name: str
    age: int
    height: float
    weight: float
    # addresses: list[str] = [] Cant't make this
    addresses: list[str] = field(
                                 default_factory= list,
                                #  repr= False # Wont will be printed in the repr
                                 )


def main() -> None:
    """Function used to run the main code."""
    p1 = Person('lucas', 23, 1.66, 50.5)
    print(p1)
    p1.addresses.append('my first address')
    print(p1)



if __name__ == '__main__':
    main()