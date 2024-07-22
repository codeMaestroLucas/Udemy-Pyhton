from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def add_user(self, user): ...

    @abstractmethod
    def send_msg(self, msg: str, user): ...

class ChatRoom(Mediator):
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_msg(self, sender, message: str):
        for user in self.users:
            if user != sender:
                user.receive_msg(message)