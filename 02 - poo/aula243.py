"""
Its better to use Composition than Heriatage, but this is one of the ways.

class MyReprMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        
        return class_repr

class SuperTime:
    ...

class Time(SuperTime, MyReprMixin):
    def __init__(self, name: str) -> None:
        self.name = name

class Planet(MyReprMixin):
    def __init__(self, name: str) -> None:
        self.name = name
"""
def my_repr(cls):
    def __repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}: ({class_dict})'
        
        return class_repr
    
    cls.__repr__ = __repr
    return cls

def my_planet(method):
    def wrapper(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        
        if 'Terra' in result:
            return "U're in home."
        
        return result
    
    return wrapper

@my_repr
class Planet:
    def __init__(self, name: str) -> None:
        self.name = name
        
    @my_planet
    def say_name(self):
        return f'The name of the planet is {self.name}.'

if __name__ == '__main__':
    p1 = Planet('Marte')
    print(p1, )
    
    p2 = Planet('Terra')
    print(p2)
    
    print(p1.say_name())
    print(p2.say_name())