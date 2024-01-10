'''class Students ():
    def __init__ (self,name,grades):
        self.name=name
        self.grades=grades

    def print_info (self):
        print(f"Student: {self.name} has notes: {self.grades}")

    def average(self):
        aver=sum(self.grades)/len(self.grades)
        print(f"The average note of the student {self.name} is {aver} ")

student1= Students ("Ivan",[4,3,2,2,5])
student1.print_info()
student1.average()'''

'''class InventoryItem ():
    def __init__(self,name,price,colour,quantity):
        self.name=name
        self.price=price
        self.colour=colour
        self.quantity=quantity
    def print_info (self):
        print(f"This is {self.colour} {self.name}. It costs {self.price}. There are {self.quantity} pieces.")

    def total(self):
        total=sum(self.price)
        print(f"The total sum is {total}")
    
    def addItem (self,name):
        listofproducts.append(name=InventoryItem(self.name,self.price,self.colour,self.quantity))

item1=InventoryItem ("Cake",20.000,"white",10)
item2=InventoryItem ("Cupcake",10.000,"pink",7)
item3=InventoryItem ("Ice-cream",30.000,"red",9)
item4=InventoryItem ("Pie",50.000,"orange",8)
listofproducts=(item1,item2,item3,item4)

item1.print_info()
print()'''

'''dictionary=dict()
class Calender ():
    def addItem(date,event):
        dictionary[date]=event
    def searchItem (date,event):
        if date in dictionary:
            print(f"This date {date} has an event : {event}")
    def deleteItem(date,event):
        dictionary[date]=event

day1= Calender ("20.12.2023, birthday")
day2= Calender ("10.12.2023, anniversary")
day3= Calender ("05.12.2023, wedding")
day4= Calender ("31.12.2023, New year")

day1.print_info()
print()'''

maps = [1,2,3,
        4,5,6,
        7,8,9]

victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]

def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])
 
    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])
 
    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])
 

def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol
 
def get_result():
    win = ""
 
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"

    return win

 
game_over = False
player1 = True
 
while game_over == False:
 
    # 1. Показываем карту
    print_maps()
 

    if player1 == True:
        symbol = "X"
        step = int(input("Человек 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Человек 2, ваш ход: "))
 
    step_maps(step,symbol) # делаем ход в указанную ячейку
    win = get_result() # определим победителя
    if win != "":
        game_over = True
    else:
        break
    
        
 
    player1 = not(player1)