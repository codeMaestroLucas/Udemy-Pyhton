from state import State, Draft

class Document:
    def __init__(self) -> None:
        self.state: State = Draft()

    def set_state(self, new_state: State) -> None:
        self.state = new_state
        print(f"Document state changed to: \
\033[33m{self.state.__class__.__name__}\033[m"
            , end='\n'*2)

    def publish(self) -> None:
        self.state.publish(self)

    def reject(self) -> None:
        self.state.reject(self)