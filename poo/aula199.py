class Person:
    def __init__(self, name: str, lastname: str, age: int):
        self.name = name
        self.lastname = lastname
        self.age = age

class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

if __name__ == "__main__":
    pq = Person('Jhon', 'Due', 31)
    car1 = Car('Volkswagen', 'Fusca', 1987)

    print(pq.name, pq.lastname, pq.age)
    
