from math import sqrt
from pegs import RoundPeg, SquarePeg


class SquarePegAdapter(RoundPeg):
    def __init__(self, peg: SquarePeg) -> None:
        super().__init__(peg.width *  sqrt(2) /2)
        self.peg = peg
    
