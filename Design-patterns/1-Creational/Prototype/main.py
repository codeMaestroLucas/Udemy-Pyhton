from shapes import Rectangle, Circle

def main() -> None:
    """Function used to run the main code."""
    original_circle: Circle = Circle(15)
    original_rectangle: Rectangle = Rectangle(10, 20)

    print(f'Original Circle: {original_circle}')
    print(f'Original Rectangle: {original_rectangle}')

    print('='*60, f'\n{"CLONES":^60}\n', '='*60)

    other_circle: Circle = original_circle.clone()
    other_rectangle: Rectangle = original_rectangle.clone()

    print(f'Other Circle: {other_circle}')
    print(f'Other Rectangle: {other_rectangle}')


if __name__ == '__main__':
    main()