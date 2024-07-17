from math import sqrt
from pegs import RoundPeg, SquarePeg


class SquareToRoundPegAdapter(RoundPeg):
    def __init__(self, peg: SquarePeg) -> None:
        self.peg = peg
        
    def get_radius(self) -> float:
        return self.peg.width * sqrt(2) / 2