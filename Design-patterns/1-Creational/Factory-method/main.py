from fac_method import AnimalFactory
from animals import Animal


def main() -> None:
    """Function used to run the main code."""
    factory: AnimalFactory = AnimalFactory()

    print(f'DOG)\n')
    
    dog: Animal = factory.create_an_animal("dog", "kiko")

    print(dog)
    print(dog.say_hi())

    print("-"*50, end='\n'*3)


    print(f'CAT)\n')
    
    cat: Animal = factory.create_an_animal("cat", "cookie")

    print(cat)
    print(cat.say_hi())

    print("-"*50)



if __name__ == '__main__':
    main()