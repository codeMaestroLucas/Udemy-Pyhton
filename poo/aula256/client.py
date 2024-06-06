from account import Account
from abc import ABC

class Person(ABC):
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age
        
class Client(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self._account = None
        
    @property
    def account(self) -> None:
        return self._account
    
    @account.setter
    def account(self, account: Account) -> None:
        self._account = account
        
if __name__ == '__main__':
    p1 = Client('LUCAS', 123)
    p1.name = 'Lucas'
    p1.age = 23
    print(p1.__dict__)