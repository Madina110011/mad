'''dictionary={"Фролов":"Александр","Беляев":"Алик","Прушинский":"Евгений","Добролюбов":"Сергей"}
print(dictionary)
del dictionary["Фролов"]
print(dictionary)''' 

'''aa={1001:["лук","2 кг","200 тг"], 1002:["хлеб","2 булки ","300 тг"], 1003:["молоко"," 2 л","400 тг"], 1004:["бананы","1 кг ","600 тг"]}
print(aa)
for number in aa.keys():
    print(f"{number}: товар {aa[number][0]}, количество {aa[number][1]}, стоимость {aa[number][2]}")'''

'''list1={1,2,3,4,5,6,7,8,9}
list2={1,12,3,4,67,35,8,9}
print("difference: ",list1.difference(list2))
print("union: ", list1.union(list2))'''

'''aaa={
    1001:"мука", 
    1002:"хлеб", 
    1003:"молоко", 
    1004:"яблоки"
    }
ID=int(input("Input ID: "))
if ID in aaa:
    print(f"Товар под номером ID {ID} - {aaa[ID]}")
else:
    print ('Not found')'''

'''list1={1,2,3,4,5,6,7,8,9}
list2={1,12,3,4,67,35,8,9}
print(list1.intersection(list2))'''

'''World={"Казахстан":["Астана","Алмата","Караганда"]}
new_country = input("Пожалуйста, введите добавляемую страну: ")
cities = input("Пожалуйста, введите города через запятую: ").split(',')
World[new_country]=cities
print(World)''' 

'''list={"мука":1000, "хлеб":200, "молоко":400, "яблоки":600}
prices=list.values()
sum=0
i=int
for i in list.values():
    sum=sum+i
print(sum)''' 

'''list1={1,2,3,4,5,6,7,8,9}
list2={1,12,3,4,67,35,8,9}
print(list1.symmetric_difference(list2))'''