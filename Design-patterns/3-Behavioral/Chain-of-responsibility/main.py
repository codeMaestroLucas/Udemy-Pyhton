from handler import Handler, MonkeyHandler, SquirrelHandler, DogHandler

def client_code(handler: Handler) -> None:
    for food in ['Nut', 'Banana', 'Coffee']:
        print(f'Client is asking for {food}')
        
        result = handler.handle(food)

        if result:
            print(f"{result}")
        else:
            print(f'The {food} was left untouched.')
        
        print('-'*60, end='\n\n')


def main() -> None:
    """Function used to run the main code."""
    monkey: MonkeyHandler = MonkeyHandler()
    squirrel: SquirrelHandler = SquirrelHandler()
    dog: DogHandler = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")


if __name__ == '__main__':
    main()