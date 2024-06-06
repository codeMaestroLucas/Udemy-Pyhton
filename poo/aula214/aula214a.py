class Tool_to_Write:
    def __init__(self, name: str) -> None:
        self.name = name


class Writer:
    def __init__(self, name: str) -> None:
        self.name = name
        self._tool_to_write = None
        
    @property
    def tool_to_write(self):
        return self._tool_to_write
    
    @tool_to_write.setter
    def tool_to_write(self, tool: Tool_to_Write):
        self._tool_to_write = tool
        print(f'The writer {self.name} is now writing with {tool.name}.')
        
    def write(self, msg: str):
        if self._tool_to_write is None:
            print(f'The writer {self.name} cant write without an writing tool.')
            return
        
        print(f'The writer {self.name} wrote \033[1m{msg}\033[m with {self._tool_to_write.name}.')
        
if __name__ == '__main__':
    pencil = Tool_to_Write('pencil')
    pen = Tool_to_Write('pen')
    
    w1 = Writer('Stephen King')
    
    w1.write('Hello world')
    
    w1.tool_to_write = pencil
    w1.tool_to_write = pen
    
    w1.write('Hello world')
    