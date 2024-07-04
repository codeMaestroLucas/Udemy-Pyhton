from threading import Thread, Lock

class Tickes:
    def __init__(self, quantity: int) -> None:
        self.quantity = quantity
        self.lock = Lock()

    def buy_ticket(self, quantity_to_buy: int) -> None:
        self.lock.acquire() # Ensures that all the Threads that iniciate this
        # function will execute it entirely.
        
        if quantity_to_buy <= self.quantity:
            self.quantity -= quantity_to_buy
            print(f'{quantity_to_buy} tickets were bought.\n\
{self.quantity} tickets left\n')

        else:
            print(f'Only have {self.quantity} tickets left.')

        self.lock.release()
        
def main() -> None:
    """Function used to run the main code."""
    from time import sleep

    tickets = Tickes(20)

    for c in range(1, 11):
        t: Thread = Thread(target= tickets.buy_ticket(c), args= (c, ))

        t.start()
        sleep(1)
    

    print(tickets.quantity)


if __name__ == '__main__':
    main()