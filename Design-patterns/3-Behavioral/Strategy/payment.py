from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None: ...


class CreditCardPayment(PaymentStrategy):
    def __init__(self, name: str,
                 card_number: str,
                 cvv: str,
                 expiry_date: str) -> None:
        self._name = name
        self._card_number = card_number
        self.cvv = cvv
        self._expiry_date = expiry_date
        
    def pay(self, amount: float) -> None:
        print(f'Credit payment of ${amount:.2f} using Credit Card.')


class CashPayment(PaymentStrategy):

    def pay(self, amount: float) -> None:
        print(f'Payment of ${amount:.2f} using Cash.')