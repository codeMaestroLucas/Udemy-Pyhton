from typing import List
from abc import ABC, abstractmethod
from client import Person, Client
from account import Account, Current_Account, Savings_Account

class Bank(ABC):
    def __init__(self, name: str) -> None:
        self._name = name
        self._accounts: List[Account] = []
        self._clients: List[Person] = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    
    def add_client(self, client: Client):
        ...

if __name__ == '__main__':
    help(Bank)
    