from typing import List

## RELAÇÕES ENTRE CLASSES ##

#! 1) Associação - uma classe se liga com a outra, mas não são dependentes entre si. Relação fraca.
class Tool_to_write:
    def __init__(self, name_tool: str):
        self._name_tool = name_tool
        
    def write(self):
        return f'The {self._name_tool} is written.'
    
    
class Writer:
    def __init__(self, name: str):
        self._name = name
        self._tool = None
        
    @property
    def tool(self):
        return self._tool
    
    @tool.setter
    def tool(self, tool: Tool_to_write):
        self._tool = tool

w1 = Writer('Lucas')
t1 = Tool_to_write('Pencil')
w1.tool = t1
print(w1.tool.write())

#! 2) Agregação - cada objeto funciona independente, mas determinadas tarefas precisam que os dois objetos estejam juntos. Tipo de Associação.
class Products:
    def __init__(self, name: str, price: float, quantity: int = 1):
        self._name = name
        self._price = price
        self._quantity = quantity
        

class Shopping_Cart:
    def __init__(self, products: List[Products] = []):
        self._products = products
    
    def total_value(self) -> str:
        total: float = sum(p._price * p._quantity for p in products)
        
        return f'Total ---- \033[1;32m${total:.2f}\033[m'

    def list_products(self) -> None:
        for product in self._products:
            print(product.__dict__)


p1 = Products('feijao', 13.86, 4)
p2 = Products('arroz', 19.5, 2)
p3 = Products('carne', 45, 3)

products = [p1, p2, p3]

sh = Shopping_Cart(products)

sh.list_products()
print(sh.total_value())

#! 3) Composição - As partes são totalmente dependentes uma da outra. Especialização da Agregação.

class Address:
    def __init__(self, street: str, number: int):
        self._street = street
        self._number = number
        
class Client:
    def __init__(self, name: str):
        self._name = name
        self._addresses: List[Address] = []
        
    def add_address(self, street:str , number:int):
            
        self._addresses.append(Address(street, number)) # Dessa forma ao excluir a classe, as instâncias de Addresses vão deixar de existir tbm
        
    def show_address(self):
        for address in self._addresses:
            print(address.__dict__)
            
c1 = Client("John")

c1.add_address("San Francisco", 123)
c1.add_address("São Paulo", 456)
c1.add_address("Rio de Janeiro", 789)

c1.show_address()