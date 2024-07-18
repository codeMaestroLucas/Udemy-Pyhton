from abc import ABC

class Handler(ABC):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return self._next_handler

    def handle(self, request: any):
        if self._next_handler:
            return self._next_handler.handle(request)
        
        
class MonkeyHandler(Handler):
    def handle(self, request: any) -> str:
        if request == 'Banana':
            return 'Monkey: I am eating the Banana'

        return super().handle(request)


class SquirrelHandler(Handler):
    def handle(self, request: any) -> str:
        if request == 'Nut':
            return 'Squirrel: I am eating the Nut'

        return super().handle(request)


class DogHandler(Handler):
    def handle(self, request: any) -> str:
        if request == 'MeetBall':
            return 'Dog: I am barking at the MeetBall'

        return super().handle(request)