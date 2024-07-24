from payment import PaymentStrategy

class ShoppingCart:
    def __init__(self) -> None:
        self.items: list = []
        self.total_amount: float  = 0

    def add_item(self, item_name: str, price: float) -> None:
        self.items.append(item_name)
        self.total_amount += price
    
    def get_total_amount(self) -> float:
        return self.total_amount
    
    def make_payment(self, payment_strategy: PaymentStrategy) -> None:
        amount = self.get_total_amount()
        payment_strategy.pay(amount)