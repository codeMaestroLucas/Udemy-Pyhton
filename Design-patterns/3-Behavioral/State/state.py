from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from document import Document


class State(ABC):
    @abstractmethod
    def publish(self, document: 'Document') -> None:
        pass

    @abstractmethod
    def reject(self, document: 'Document') -> None:
        pass


class Draft(State):
    def publish(self, document: 'Document') -> None:
        print('The document is under review.')
        document.set_state(Moderation())

    def reject(self, document: 'Document') -> None:
        print('The document is already in draft state.')


class Moderation(State):
    def publish(self, document: 'Document') -> None:
        print('The document is now published!')
        document.set_state(Published())

    def reject(self, document: 'Document') -> None:
        print('Document review rejected, back to draft state.')
        document.set_state(Draft())


class Published(State):
    def publish(self, document: 'Document') -> None:
        print('The document is already in publish state.')

    def reject(self, document: 'Document') -> None:
        print('Publisheds documents cannot be rejected.')