import json

# Used to create an class and export it to a JSON file

path: str = r'.\poo' + r'\pessoa.json'

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def export_to_json(self):
        with open(path, 'w', encoding='utf8') as file:
            json.dump(self.__dict__, file, ensure_ascii=False, indent=4)
            
if __name__ == "__main__":
    p1 = Person('Lucas', 23)
    p1.export_to_json()