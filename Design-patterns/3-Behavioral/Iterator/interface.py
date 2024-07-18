from aggregate import Aggregate
from iterator import Iterator

class NameCollection(Aggregate):
    def __init__(self):
        self._names = []
        
    def add_name(self, name: str) -> None:
        self._names.append(name)
        
    def create_iterator(self):
        return NameIterator(self)
    
    
class NameIterator(Iterator):
    def __init__(self, collection: NameCollection):
        self._collection = collection
        self._current_index = 0
        
    def has_next(self) -> bool:
        return self._current_index < len(self._collection._names)

    def next(self):
        if self.has_next():
            name = self._collection._names[self._current_index]
            self._current_index += 1
            return name
        
        raise StopIteration