from color import Color, Red, Blue
from shapes import Shape, Square, Circle


def main() -> None:
    """Function used to run the main code."""
    red: Color = Red()
    blue: Color = Blue()
    
    blue_square: Shape = Square(blue)
    blue_circle: Shape = Circle(blue)
    
    red_square: Shape = Square(red)
    red_circle: Shape = Circle(red)
    
    print(blue_square.draw())
    print(blue_circle.draw())
    print(red_square.draw())
    print(red_circle.draw())
    




if __name__ == '__main__':
    main()