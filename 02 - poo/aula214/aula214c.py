from typing import List

class Address:
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


class Client:
    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List[Address] = []
        
    def show_address(self) -> None:
        print()
        print('='*20)
        print(f'{"ADDRESSES":^20}')
        print('-'*20)
        for c, addr in enumerate(self._addresses):
            print(f'{c + 1:>3}. {addr.street} st, n {addr.number}º')
        print('='*20)
        print()

    def add_address(self, street: str, number: str) -> None:
        for addr in self._addresses:
            if addr.street == street and addr.number == number:
                print("The address allredy is in the list of addresses.")
                return
        
        self._addresses.append(Address(street, number))

    def remove_address(self, street: str, number: str) -> None:
        for c, addr in enumerate(self._addresses):
            if addr.street == street and addr.number == number:
                pos: int = c
                self._addresses.__delitem__(pos)

                print("The address is now removed of list of addresses.")
                return

        print("The address inst in the list of addresses.")
            

if __name__ == '__main__':
    c1 = Client('Lucas')
    
    c1.add_address('DF', 123)
    c1.add_address('SP', 456)
    c1.show_address()

    c1.remove_address('SP', 123)
    c1.remove_address('SP', 456)

    c1.show_address()

    c1.add_address('DF', 123)
    c1.add_address('DF', 456)
    c1.show_address()