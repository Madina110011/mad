class Car():
    def __init__(self,brand,model,year):
       self.brand=brand
       self.model=model
       self.year=year
    
    def description(self):
        print(f"This car is {self.brand} {self.model}, the model year of the car is {self.year}")

car1= Car("Toyota","Camry",2020)
car2= Car("Mitsubishi","Pajero",2010)

car1.description()
car2.description()

class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name, age)
        self.salary=salary
    def get_info(self):
        return(f"This is {self.name},who is {self.age} and this employee earns {self.salary}")
    
employee1= Employee("Max",20, 200.000)
employee2= Employee("Pat",30,300.000)
employee3= Employee("Sam",40,400.000)

print(employee3.get_info())

class Animal():
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return(f"{self.name} goes woof")
class Cat(Animal):
    def speak(self):
        return(f"{self.name} goes meow")
dog=Dog("Fluffy")
cat=Cat("Cloud")

dog.speak()
cat.speak()
