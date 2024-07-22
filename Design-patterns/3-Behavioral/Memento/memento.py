class Memento:
    def __init__(self, state: str) -> None:
        self._state = state
    
    def get_state(self) -> str:
        return self._state