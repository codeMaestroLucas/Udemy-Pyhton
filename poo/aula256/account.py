from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, agency: str, acc_number: int) -> None:
        self._agency = agency
        self._acc_number = acc_number
        self._balance = 0
    
    @property
    def agency(self):
        return self._agency
    
    @agency.setter
    def agency(self, agency):
        self._agency = agency
    
    @property
    def acc_number(self):
        return self._acc_number
    
    @acc_number.setter
    def acc_number(self, acc_number):
        self._acc_number = acc_number
        
    def deposit(self, to_deposit: float) -> None:
        if to_deposit > 0:
            self._balance += to_deposit
            print(f'Successfully deposit \033[32m${to_deposit:.2f}\033[m.')
            
            return
        
        print('Something went wrong.')
    
    @abstractmethod
    def withdraw(self, to_withdraw: float): ...
    
    
class Current_Account(Account):
    def __init__(self, agency: str, acc_number: int) -> None:
        super().__init__(agency, acc_number)
        

    
    def withdraw(self, to_withdraw: float):
        ...



"""
Current Account or Savings Account
"""

if __name__ == '__main__':
    ca = Current_Account('12345FD', 9876)
    ca.deposit(70)
    print(ca.__dict__)