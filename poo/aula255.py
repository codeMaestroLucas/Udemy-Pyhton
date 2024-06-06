# Enum

from enum import Enum, auto
from typing import List

class Directions(Enum):
    
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
    OTHER = auto() # Another way to enumerate automaticlly

if __name__ == '__main__':
    direction = Directions
    print(direction.LEFT, direction(1), direction['LEFT'])
    print(f'NAME= {direction.RIGHT.name}, VALUE= {direction.RIGHT.value}')
    
    