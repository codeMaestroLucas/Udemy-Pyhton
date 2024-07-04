# __call__ Method

class ClassMe:
    def __init__(self, phone: str) -> None:
        self.phone = phone
    
    
    def __call__(self, *args, **kwargs):
        print(f'Calling {self.phone}')
    
if __name__ == '__main__':
    c = ClassMe('23456')
    c() # Now the class is callable