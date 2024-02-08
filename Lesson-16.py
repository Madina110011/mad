from abc import abstractmethod


class Vehicle():
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def print_avto(self):
        print(self.model, self.year)

class Car(Vehicle):
    def __init__(self, model, year, fuel_type):
        super().__init__(model, year) 
        self.fuel_type = fuel_type

    def print_avto(self):
        print(self.model, self.year, self.fuel_type)

vehicle = Vehicle("Tesla", 2022)
car = Car("Tesla", 2022, "electricity")

vehicle.print_avto()
car.print_avto()

# 2. 

class Animal(abs):
    @abstractmethod 
    def speak(self):
        pass
class Flyable(abs):
    @abstractmethod
    def fly(self):
        pass 

class Bird(Animal):
    def speak(self):
        return ("Чирик-чирик")

class Bird(Flyable):
    def fly(self):
        return ("The bird is flying")
    
bird = Bird()
print(bird.speak())
print(bird.fly())
