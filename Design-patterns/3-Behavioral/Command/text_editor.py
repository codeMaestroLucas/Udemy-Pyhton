class TxtEditor:
    def __init__(self):
        self.text: str = ''

    def write_txt(self, txt_to_write: str) -> None:
        self.text += txt_to_write
        
    def erase_txt(self, txt_to_erase: str) -> None:
        if txt_to_erase in self.text:
            self.text = self.text.replace(txt_to_erase, '')
        
    def get_txt(self) -> str:
        return self.text