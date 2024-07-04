from account import Account, Current_Account, Savings_Account
from abc import ABC

class Person(ABC):
    def __init__(self, name: str, age: int) -> None:
        self._name = name.title().strip()
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
        self._account: Account | None = None
        
    @property
    def account(self) -> Account | None:
        return self._account
    
    @account.setter
    def account(self, account: Account) -> None:
        self._account = account
        
if __name__ == '__main__':
    c1 = Savings_Account(agency= 'agencia', acc_number= 123, limit= 100)
    p1 = Client('LUCAS', 123)
    p1.age = 23
    print(p1.__dict__)
    p1.account = c1
    print(p1.__dict__)