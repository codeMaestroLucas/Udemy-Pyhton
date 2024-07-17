from abc import ABC

class Peg(ABC): ...

class RoundPeg(Peg):
    def __init__(self, radius: float):
        self.radius = radius
        
    def get_radius(self) -> float:
        return self.radius


class SquarePeg(Peg):
    def __init__(self, width: float):
        self.width = width

    def get_widht(self) -> float:
        return self.width