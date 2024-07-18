from abc import ABC, abstractmethod
from text_editor import TxtEditor


class Command(ABC):
    @abstractmethod
    def execute(self): ...
    
    @abstractmethod
    def undo(self): ...


class WriteCommand(Command):
    def __init__(self, editor: TxtEditor, text: str):
        self.editor = editor
        self.text = text
        
    def execute(self):
        self.editor.write_txt(self.text)
    
    def undo(self):
        self.editor.erase_txt(self.text)


class TextEditorInvoker:
    def __init__(self):
        self.commands = []
        
    def execute_command(self, command: Command):
        command.execute()
        self.commands.append(command)
        
    def undo_last_command(self):
        if self.commands:
            last_command = self.commands.pop()
            last_command.undo()