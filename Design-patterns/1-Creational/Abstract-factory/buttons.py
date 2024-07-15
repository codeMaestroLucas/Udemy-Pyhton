from abc import ABC, abstractmethod

class Button(ABC):
    """Abstract class of buttons.
    """
    @abstractmethod
    def click(self):
        pass
    
    
class WinButton(Button):
    """Specific windows button.

    Args:
        Button (_type_): Abstract class of button.
    """
    def click(self):
        return "Windows button clicked"
        
        
class MacButton(Button):
    """Specific macOS button.

    Args:
        Button (_type_): Abstract class of button.
    """
    def click(self):
        return "MacOS button clicked"