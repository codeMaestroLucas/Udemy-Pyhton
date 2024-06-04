class Person:
    YEAR = 2024
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        
    @classmethod
    def say_hi(cls):
        print('hi')
        
    @classmethod
    def create_elder(cls, name: str):
        return cls(name, 70)
    
    @classmethod
    def create_anonymous(cls, age: int):
        return cls('Anonymous', age)
    
if __name__ == "__main__":
    p1 = Person('John', 20)
    p2 = Person.create_elder('Jane')
    p3 = Person.create_anonymous(30)
    print(p1.name, p1.age)
    print(p2.name, p2.age)
    print(p3.name, p3.age)
    print(p1.YEAR)
    Person.say_hi()