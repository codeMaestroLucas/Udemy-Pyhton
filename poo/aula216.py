# Herança Simples
class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
        
    def say_class_name(self):
        print(self.__class__.__name__)
    
    
class Student(Person):
    def __init__(self, name: str, age: int, class_name: str):
        self._name = name
        self._age = age
        self._class_name = class_name

s1 = Student('Lucas', 23, 'math')
print(s1.__dict__)
s1.say_class_name()

print()

p1 = Person('Joao', 31)
print(p1.__dict__)
p1.say_class_name()