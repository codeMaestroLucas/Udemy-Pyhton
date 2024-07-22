from mediator import ChatRoom
from user import User

def main() -> None:
    """Function used to run the main code."""
    mediator: ChatRoom = ChatRoom()

    user1: User = User('Alice', mediator)
    user2: User = User('Bob', mediator)
    user3: User = User('Jhon', mediator)
    
    mediator.add_user(user1)
    mediator.add_user(user2)
    mediator.add_user(user3)

    user1.send_msg('Hello Bob!')
    print()
    user2.send_msg('Hello Alice!')


if __name__ == '__main__':
    main()