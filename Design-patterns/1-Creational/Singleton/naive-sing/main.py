from nv_sing import Singleton

def main() -> None:
    """Function used to run the main code."""
    s1: Singleton = Singleton('First instance')
    print(s1)

    s2: Singleton = Singleton('Second instance')
    print(s2)


    print(s1 is s2)


if __name__ == '__main__':
    main()