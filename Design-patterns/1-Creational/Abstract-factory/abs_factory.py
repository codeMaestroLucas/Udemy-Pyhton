from abc import ABC, abstractmethod
from buttons import Button, WinButton, MacButton
from checkboxes import Checkbox, WinCheckbox, MacChecbox


class GUIFactory(ABC):
    """Abstract factory used to create the family of an specified object.
    """
    @abstractmethod
    def create_button(self) -> Button:
        """Function used to create and return an specific object of button.
        """
        pass
    
    def create_checkbox(self) -> Checkbox:
        """Function used to create and return an specific object of checkbox.
        """
        pass
    
    
class WindowsFactory(GUIFactory):
    """Specific windows factory used to create an family of windows objects.

    Args:
        GUIFactory (_type_): Abstract factory.
    """
    def create_button(self):
        return WinButton()
    
    def create_checkbox(self):
        return WinCheckbox()
    
    
class MacFactory(GUIFactory):
    """Specific mac factory used to create an family of mac objects.

    Args:
        GUIFactory (_type_): Abstract factory.
    """
    def create_button(self):
        return MacButton()
    
    def create_checkbox(self):
        return MacChecbox()