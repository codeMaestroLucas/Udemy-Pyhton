from color import Red, Blue
from shapes import Square, Circle


def main() -> None:
    """Function used to run the main code."""
    red: Red = Red()
    blue: Blue = Blue()
    
    blue_square: Square = Square(blue)
    blue_circle: Circle = Circle(blue)
    
    red_square: Square = Square(red)
    red_circle: Circle = Circle(red)
    
    print(blue_square.draw())
    print(blue_circle.draw())
    print(red_square.draw())
    print(red_circle.draw())


if __name__ == '__main__':
    main()