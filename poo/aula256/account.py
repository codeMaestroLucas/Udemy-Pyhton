from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, agency: str, acc_number: int) -> None:
        self._agency = agency
        self._acc_number = acc_number
        self._balance = 0
    
    @property
    def agency(self) -> None:
        return self._agency
    
    @agency.setter
    def agency(self, agency) -> None:
        self._agency = agency
    
    @property
    def acc_number(self) -> None:
        return self._acc_number
    
    @acc_number.setter
    def acc_number(self, acc_number) -> None:
        self._acc_number = acc_number
     
    @abstractmethod
    def deposit(self, to_deposit: float) -> None:
        if to_deposit > 0:
            self._balance += to_deposit
            print(f'Successfully deposit \033[32m${to_deposit:.2f}\033[m.')
            
            return
        
        print('Something went wrong.')
    
    @abstractmethod
    def withdraw(self, to_withdraw: float) -> None:
        self._balance -= abs(to_withdraw)
        print(f'Successfully withdraw \033[32m${to_withdraw:.2f}\033[m.')
        
    
class Current_Account(Account):
    def __init__(self, agency: str, acc_number: int) -> None:
        super().__init__(agency, acc_number)

    def deposit(self, to_deposit: float) -> None:
        return super().deposit(to_deposit)
    
    def withdraw(self, to_withdraw: float) -> None:
        return super().withdraw(to_withdraw)


class Savings_Account(Account):
    def __init__(self, agency: str, acc_number: int) -> None:
        super().__init__(agency, acc_number)
    
    def deposit(self, to_deposit: float) -> None:
        super().deposit(to_deposit)
    
    def withdraw(self, to_withdraw: float) -> None:
        if self._balance - to_withdraw <= 0:
            print(f"Cant withdraw more than \033[31m${self._balance:.2f}\033[m from your account.")
            return
        
        self._balance -= abs(to_withdraw)