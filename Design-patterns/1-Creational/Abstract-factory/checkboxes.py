from abc import ABC, abstractmethod

class Checkbox(ABC):
    """Abstract class of checkboxes.
    """
    @abstractmethod
    def check(self):
        pass
    
    
class WinCheckbox(Checkbox):
    """Specific windows checkbox.

    Args:
        Checkbox (_type_): Abstract class of checkbox.
    """
    def check(self):
        return "Windows Checkbox checked"


class MacChecbox(Checkbox):
    """Specific MacOS checkbox.

    Args:
        Checkbox (_type_): Abstract class of checkbox.
    """
    def check(self):
        return "MacOS Checkbox checked"