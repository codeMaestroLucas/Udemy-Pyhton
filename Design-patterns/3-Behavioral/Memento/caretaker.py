from text import TextEditor
from memento import Memento

class CareTaker:
    def __init__(self, editor: TextEditor):
        self._editor = editor
        self._history = [editor.save()]

    def save(self):
        self._history.append(self._editor.save())
        
    def undo(self):
        if self._history:
            self._editor.undo(self._history.pop())
        else:
            print("No more states to undo.")