from shopping_cart import ShoppingCart
from payment import CreditCardPayment, CashPayment

def main() -> None:
    """Function used to run the main code."""
    cart: ShoppingCart = ShoppingCart()
    cart.add_item('Book of Python', 67.9)
    cart.add_item('Glass', 13.9)
    cart.add_item('Pen', 9)

    credit_card: CreditCardPayment = CreditCardPayment(name= "John Doe",
                                                       card_number= "1234567890123456",
                                                       cvv= "123",
                                                       expiry_date= "12/25")
    cart.make_payment(credit_card)

    print('-'*60, end= '\n'*2)
    
    cash: CashPayment = CashPayment()
    cart.make_payment(cash)



if __name__ == '__main__':
    main()