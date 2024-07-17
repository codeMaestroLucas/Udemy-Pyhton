from composite import File, Directory

def main() -> None:
    """Function used to run the main code."""
    f1: File = File('main.py')
    f2: File = File('app.py')
    f3: File = File('save.py')
    f4: File = File('load.py')

    d1: Directory = Directory('System_app')
    
    d1.add(f1)
    d1.add(f2)
    d1.add(f3)
    d1.add(f4)

    print(d1.show_details())

    print('-'*25)

    d1.remove_file(f3)

    print(d1.show_details())
    print('-'*25)
    
    d2: Directory = Directory('Subdirectory')
    f5: File = File('subfile.txt')
    
    d2.add(f5)
    
    d1.add(d2)

    print(d1.show_details())
    print('-'*25)

if __name__ == '__main__':
    main()