# NAMEDTUPLES
# Used to make classes of objects that just contain the values of the att, and
# dont have any method.

from collections import namedtuple
from typing import NamedTuple

Person = namedtuple('Person', ['name', 'age'])

Card = namedtuple('Card', ['value', 'naipe'])


p1 = Person('Lucas', 23)

as_espadas = Card('J', 'Heart')

print(p1)
print(as_espadas._fields) # To access the operations and the values of the
#instance u need the '_'.
print(as_espadas._asdict())
print(as_espadas._replace(naipe='Spade'))

class Car(NamedTuple): # Preffer using this insted of the above
    model: str= "MODEL" # Default value
    year: int = 2021 # Default value