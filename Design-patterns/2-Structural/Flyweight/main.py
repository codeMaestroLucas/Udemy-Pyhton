from character import CharacterFactory


def main() -> None:
    """Function used to run the main code."""
    char_fac: CharacterFactory = CharacterFactory()
    
    a1 = char_fac.get_character('A', 'arial')
    a2 = char_fac.get_character('A', 'arial')
    b = char_fac.get_character('b', 'serifa')

    print(a1.render(13))
    print(a2.render(3))
    print(b.render(13))

    print(a1 is a2)
    print(a1 is b)
    


if __name__ == '__main__':
    main()