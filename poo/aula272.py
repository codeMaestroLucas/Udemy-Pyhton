# ITERATOR


from collections.abc import Sequence

class MyList(Sequence):
    def __init__(self) -> None:
        self._data = {}

    def append(self, value):
        self._data[len(self._data)] = value
        

    def __getitem__(self, index):
        if index in self._data.keys():
            return self._data[index]
        raise IndexError
    
    def __setitem__(self, index, value):
        if index in self._data.keys():
            self._data[index] = value

    def __len__(self):
        return len(self._data)

def main() -> None:
    """Function used to run the main code."""
    l = MyList()
    l.append('lucas')
    l.append('carlos')
    print(l._data)
    l[0] = 'samuel'
    print(l._data)
    print(l[0])
    print(l[9])




if __name__ == '__main__':
    main()