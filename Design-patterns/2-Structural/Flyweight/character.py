class Character:
    def __init__(self, char: str, font: str) -> None:
        self.char = char
        self.font = font
        
    def render(self, size_of_font: int) -> str:
        return f'Character: {self.char} - Font: {self.font} - Size: {size_of_font}.'

class CharacterFactory:
    _characters: dict = {}

    @classmethod
    def get_character(cls, char: str, font: str):
        key = (char, font)
        
        if key not in cls._characters:
            cls._characters[key] = Character(char, font)
        
        return cls._characters[key]