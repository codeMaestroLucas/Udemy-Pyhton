from shapes import Circle, Square, Rectangle
from vistor import AreaVistor


def main() -> None:
    """Function used to run the main code."""
    shapes: list = [
        Circle(5),
        Square(10),
        Rectangle(20, 30)
    ]
    
    area_vistor: AreaVistor = AreaVistor()

    for shape in shapes:
        shape.accept(area_vistor)

if __name__ == '__main__':
    main()