from abc import ABC

class Hole(ABC):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def fits(self, peg) -> bool:
        return peg.self.radius <= self.radius


class RoundHole(Hole): ...

class SquareHole(Hole): ...

