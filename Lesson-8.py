'''my_list = [12,34,54,67,45]
summa = 0
average = 0
for item in my_list:
 summa += item

average = summa/ len(my_list)
print("сумма:",summa)
print("Среднее значение:",average)''' 

'''sotrudniki = ('Шакенов','Секеманов','Ильина')
for sotr in sotrudniki:
    print (sotr)''' 

'''a = [54, 78, 64, 30, 97, 69, 25, 15]
print("A =", a)
b = []
for i in a:
    if 20 < i < 90:
        a.remove(i)
        b.append(i)
print("A =", a)
print("B =", b)'''

'''frut=['lime','orange','avocado','banana','pear']
print(frut)
for f in frut:
    x=len(f)
    if x<=5:
        frut.remove(f)
print('new list',frut)''' 

'''студенты=[('Маша', 5),('Саша', 4)]
for inf in студенты:
    print (inf)''' 

'''number =[]
for i in range (0,21):
    if i%2==0:
        number.append(i)
print (number)'''

'''number =[]
summ= 0
for i in range (0,21):
    number.append(i)
    s= number[i]**2
    summ= summ+s
print (summ)''' 

1357913579 
2468324683 
3579435794 
4682746827 

mas = [[1, 3, 5, 7, 9, 1, 3, 5, 7, 9], [2, 4, 6, 8, 3, 2, 4, 6, 8, 3], [3, 5, 7, 9, 4, 3, 5, 7, 9, 4]]
mas2= []
for i in mas:
    mas2.append(sorted(i))
print(mas2)