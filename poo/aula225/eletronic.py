from log import LogPrintMixin

class Eletronic:
    def __init__(self, name: str):
        self._name = name
        self._turned_on = False
    
    def turn_on(self):
        if self._turned_on is False:
            self._turned_on = True
            return f"Turning on {self._name}..."
        else:
            return f"The {self._name} is alredy on."
        
    def turn_off(self):
        if self._turned_on is True:
            self._turned_on = False
            return f'Turning off {self._name}...'
        else:
            return f"The {self._name} is alredy off."

class Tv(Eletronic, LogPrintMixin):
    def turn_on(self):
        print(super().turn_on())
    
    def turn_off(self):
        print(super().turn_on())
    