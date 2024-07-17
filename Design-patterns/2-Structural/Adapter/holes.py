from abc import ABC
from pegs import RoundPeg

class Hole(ABC):
    def fits(self) -> bool: ...


class RoundHole(Hole):
    def __init__(self, radius: float) -> None:
        self.radius = radius
        
    def fits(self, peg: RoundPeg) -> bool:
        return peg.get_radius() <= self.radius
        