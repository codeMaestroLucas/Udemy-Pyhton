"""
um fabricante tem varios carros

um carro tem um fabricante
carro tem um motor

um motor pode estar em varios carros

exibir carro, motor, fabricante
"""

class Factory:
    def __init__(self, name: str):
        self._name = name
        
        
class Engine:
    def __init__(self, name: str):
        self._name = name
        
        
class Car:
    def __init__(self, name: str):
        self._name = name
        self._factory: Factory = None
        self._engine: Engine = None
        
    @property
    def factory(self):
        return self._engine
    
    @factory.setter
    def factory(self, factory: Factory):
        self._factory = factory
        
    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, engine: Engine):
        self._engine = engine
        
    def __repr__(self):
        return f"""
              CAR: {self._name}
              ENGINE: {self._engine._name}
              FACTORY: {self._factory._name}"""
              
              
if __name__ == '__main__':
    f1 = Factory('Volkswagen')
    f2 = Factory('BMW')

    e1 = Engine('motorzao')
    e2 = Engine('motorzinho')

    c1 = Car('Fusca')
    c2 = Car('Audi')

    c1.factory = f1
    c1.engine = e1
    print(c1)
    c1.engine = e2
    print(c1)

    c2.factory = f2
    c2.engine = e2
    print(c2)
    c2.factory = f1
    print(c2)
    
    
    help(c2)