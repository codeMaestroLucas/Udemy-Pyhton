from th_sing import Singleton

def main() -> None:
    """Function used to run the main code."""
    t1 = Singleton('First instance')
    print(t1)

    t2 = Singleton('Second instance')
    print(t2)
    
    print(t1 is t2)




if __name__ == '__main__':
    main()
