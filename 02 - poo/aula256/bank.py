from typing import List
from abc import ABC, abstractmethod
from client import Client, Client
from account import Account, Current_Account, Savings_Account

class Bank():
    def __init__(self,
                 name: str,
                 accounts: list[Account] | None,
                 clients: list[Client] | None) -> None:
        self._name = name
        self._accounts: list[Account] | None = accounts or [] # If is None := []
        self._clients: list[Client] | None = clients or []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    def _check_client(self, client: Client) -> bool:
        if self._clients is not None and client in self._clients:
            return True
        return False
    
    def _check_account(self, account: Account) -> bool:
        if self._accounts is not None and account in self._accounts:
            return True
        return False
    
    def _check_if_is_client_account(self,
                                    client: Client,
                                    account: Account) -> bool:
        if account is client._account:
            return True
        return False
        
    
    
    def authenticate(self, client: Client, account: Account) -> bool:
        return self._check_client(client) and \
            self._check_account(account) and \
            self._check_if_is_client_account(client, account)

if __name__ == '__main__':
    help(Bank)
    