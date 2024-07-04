# Dunder Methods

class Dot:
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y
        
    def __repr__(self):
        return f"Dot(X={self._x}, Y={self._y})"
    
    # Create the logic of the sum
    def __add__(self, other_dot):
        x = self._x + other_dot._x
        y = self._y + other_dot._y
        
        return Dot(x, y)

    # Create the logic of the subtract
    def __sub__(self, other_dot):
        x = self._x - other_dot._x
        y = self._y - other_dot._y
        
        return Dot(x, y)
    
    
if __name__ == "__main__":
    d1 = Dot(1, 4)
    d2 = Dot(4, -6)
    
    print(d1)
    print(d2, end='\n\n')
    
    
    d3 = d1 + d2
    print(d3, end='\n\n')

    d4 = d1 - d2
    print(d4)