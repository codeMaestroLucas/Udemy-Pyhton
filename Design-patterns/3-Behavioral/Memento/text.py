from memento import Memento

class TextEditor:
    def __init__(self):
        self._content = ""

    def write(self, words: str) -> None:
        self._content += words
    
    def get_content(self) -> str:
        return self._content
    
    def save(self) -> Memento:
        return Memento(self._content)

    def undo(self, memento: Memento) -> None:
        self._content = memento.get_state()
