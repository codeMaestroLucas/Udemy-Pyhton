# Classes Decorators

class Multiplicar:
    def __init__(self, multiplicador) -> None:
        self._multiplicador = multiplicador
        
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            return result * self._multiplicador
        return wrapper
            
            
class Dividir:
    def __init__(self, divisor: int) -> None:
        self.divisor = divisor if divisor != 0 else 1
        
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            return result / self.divisor
        return wrapper
    
@Multiplicar(7) # A ordem de chamadas dos decoradores influencia em como eles vão ser executados
@Dividir(9)
def soma(x: int, y: int):
    return x + y


if __name__ == '__main__':
    print(soma(1, 6))