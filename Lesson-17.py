'''num1 = 6
num2 = 4 
print(num1+num2)
str1 = "privet"
str2 = "world"
print(str1+" "+str2)
print(len) '''


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14
    
def calculate_area(shape: Shape):
    return shape.area()
