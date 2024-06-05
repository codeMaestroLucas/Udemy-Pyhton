from typing import List

class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self._name = name
        self._price = price
        self._quantity = quantity
        
class ShoppingCart:
    def __init__(self) -> None:
        self._products: List[Product] = []
    
    def show_products_in_cart(self):
        print('='*40)
        print(f"{'PRODUCTS':^40}")
        print('-'*40)
        for c, product in enumerate(self._products):
            print(f'\033[1;33m{c + 1}.\033[m {product._name:<15}\033[32m${product._price:<15.2f}\033[m {product._quantity}')
        
        print('='*40)
        
    def _check_product_on_list(self, product: Product):
        name_ = product._name
        awnser: bool = False
        pos = -1
        
        for c, added_products in enumerate(self._products):
            if added_products._name == name_:
                awnser = True
                pos = c
                
        return awnser, pos
           
    def add_product(self, product: Product):
        is_on_the_list, pos = self._check_product_on_list(product)
        
        if is_on_the_list:
            print(f'More {product._quantity} of {product._name} added to the cart.')

            to_add = self._products[pos]
            to_add._quantity += product._quantity
            
            return
            
        self._products.append(product)
        print(f'Product {product._name} added into the cart.')
        
    def remove_product(self, product: Product):
        is_on_the_list, pos = self._check_product_on_list(product)
        
        if  is_on_the_list:
            to_remove = self._products[pos]

            if to_remove._quantity - product._quantity < 0:
                print(f'Cant remove more than {product._quantity} items of {product._name} from the cart.')
                
            elif to_remove._quantity - product._quantity == 0:
                self._products.__delitem__(pos)
                print(f'Product {product._name} removed from the cart.')

            else:
                to_remove._quantity -= product._quantity
                print(f'{product._quantity} of {product._name} were removed from the cart.')
            
            return
        
        print(f'This product inst in the cart.')
        
    def total_cost(self):
        return f'TOTAL COST: \033[1;32m${sum(p._quantity * p._price for p in self._products):.2f}\033[m'


if __name__ == '__main__':
    p1 = Product('arroz', 13.5, 3)
    p2 = Product('feijao', 15.9, 2)
    p3 = Product('feijao', 15.9, 7)
    p4 = Product('carne', 45, 4)
    
    sh = ShoppingCart()
    
    sh.add_product(p1)
    sh.add_product(p2)
    sh.show_products_in_cart()

    sh.add_product(p1)
    sh.show_products_in_cart()

    sh.remove_product(p3)
    sh.remove_product(p4)

    sh.add_product(p4)
    sh.show_products_in_cart()

    print(sh.total_cost())