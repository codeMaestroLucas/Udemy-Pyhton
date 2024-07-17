from text import Text

class TextDecorator(Text):
    def __init__(self, wrapped: Text) -> None:
        self.wrapped = wrapped
        
    def render(self) -> str:
        return self.wrapped.render()


class UpperTextDecorator(TextDecorator):
    def render(self) -> str:
        return self.wrapped.render().upper()
    
    
class EndExclamationTextDecorator(TextDecorator):
    def render(self) -> str:
        return self.wrapped.render() + "!"