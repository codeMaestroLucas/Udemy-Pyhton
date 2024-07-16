from abc import ABC

class Peg(ABC):
    def __init__(self, radius: float):
        self.radius = radius
        
class RoundPeg(Peg): ...

class SquarePeg(Peg):
    def __init__(self, width: float):
        self.width = width
        