'''class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def introduce(self):
        return f"Меня зовут:{self.name}, мне: {self.age} лет" 
    
person1 = Person("Валя", 32)
person2 = Person("Саша", 29) 

greet1 = person1.introduce()
greet2 = person2.introduce()
print(greet1)
print(greet2)''' 

'''class Product:
    def __init__(self, title, description, price):
        self.title = title
        self.description = description
        self.price = price 

    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description
    
    def get_price(self):
        return self.price
    
    def set_price(self, price):
        self.price = price
    
    def get_title(self):
        return self.title        
    
    def set_title(self, title):
        self.title = title
    
    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nPrice: {self.price}"
    
product1 = Product('Iphone 15', 'Apple product, smartphone', 5000)
print(product1)
product1.set_price(100)
product1.set_description('Technology')
print(product1.get_price())
print(product1)''' 

class Book:

    def __init__(self, title, author, publication_year, is_available=True):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = is_available
        
    def chekout(self):
        self.is_available = False
        print('Книга теперь не доступна')
    
    def checkin(self):
        self.is_available = True
        print('Книга теперь доступна')
        
    def display_info(self):
        print(f"Title - {self.title}\nAuthor - {self.author}\nPublication year - {self.publication_year}\nIs available - {self.is_available}")
        
        
my_book = Book('Цветы для Элджернона', 'Даниел Киз', '2022')
my_book.display_info()
my_book.chekout()
my_book.display_info()