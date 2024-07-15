from abc import ABC


class House(ABC):
    def __init__(self) -> None:
        self.foundation = None
        self.structure = None
        self.roof = None
        self.interior = None
        self.rooms = None
        
    def __repr__(self) -> str:
        _list: list[str] = []
        
        if self.foundation:
            _list.append(f"{self.foundation} foudation")

        if self.structure:
            _list.append(f"{self.structure} structure")
            
        if self.roof:
            _list.append(f"{self.roof} roof")
            
        if self.interior:
            _list.append(f"{self.interior} interior")
            
        if self.rooms:
            _list.append(f"{self.rooms} rooms")
            
        awnser: str = "An House with "
        # awnser += ", ".join(i for i in _list)
        for c, i in enumerate(_list):
            if c == len(_list) - 1:
                awnser += f'and {i}.'

            else:
                awnser += f'{i}, '
        
        return awnser