from mediator import Mediator

class User:
    def __init__(self, name: str, mediator: Mediator) -> None:
        self._name = name
        self.mediator = mediator
    
    def send_msg(self, msg: str) -> None:
        print(f'The user {self._name} \033[31msends:\033[m {msg}')
        self.mediator.send_msg(self, msg)
    
    def receive_msg(self, msg: str) -> None:
        print(f'The user {self._name} \033[32mreceives:\033[m {msg}')