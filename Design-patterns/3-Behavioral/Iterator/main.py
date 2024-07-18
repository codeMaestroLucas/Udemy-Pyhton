from interface import NameCollection

def main() -> None:
    """Function used to run the main code."""
    name_collection = NameCollection()
    
    name_collection.add_name('Lucas')
    name_collection.add_name('Alice')
    name_collection.add_name('Jane')
    name_collection.add_name('Jhon')

    iterator = name_collection.create_iterator()

    while iterator.has_next():
        print(iterator.next())


if __name__ == '__main__':
    main()
