from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self): ...


class File(FileSystemComponent):
    def __init__(self, name: str) -> None:
        self.name = name
        
    def show_details(self):
        return f'File: {self.name}'


class Directory(FileSystemComponent):
    def __init__(self, name: str) -> None:
        self.name = name
        self.files: list[File] = []
        
    def add(self, to_add: FileSystemComponent) -> None:
        self.files.append(to_add)
        
    def remove_file(self, file: File) -> None:
        self.files.remove(file)
        
    def show_details(self):
        details: list[str] = [f'{"="*25}\nDirectory: {self.name}\n{"="*25}']
        
        for file in self.files:
            details.append(file.show_details())
        
        return '\n'.join(details)