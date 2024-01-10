'''for x in range(21):
    rez=x%2
    if rez==0:
        print(x)''' 

'''n=int(input('Введите число:'))
for i in range (11):
    print(f'{i}*{n}={i*n}')'''
    

'''name=('Python')
for l in name: 
    print(l)''' 

'''count=int(1)
x=int(0)
while count<100:
    rez=count%2
    if rez!=0:
        x=x+count
        count+=1
print(f'Сумма нечетных чисел в последовательности от 1 до 100 = {x}')'''

'''n=int(input('Введите число:'))
for x in range (n+1):
    rez=x%2
    if rez==0:
        print(f'{x}')''' 

'''count=int(1)
rez=int(0)
n=int(input('Введите число:'))
while count<=n:
    rez+=count
    count+=1
print(f'Сумма чисел в последовательности от 1 до {n} равна {rez}')''' 

'''z='*'
for i in range (5):
    for j in range (1): 
        print(z)
        z+='*'  ''' 

'''for i in range (6):
    for j in range (6): 
        if i!=0 and j!=0: 
            print(f'{j}*{i}={j*i}')
    print('\n')''' 

'''n=int(input('Введите число:'))
rez_n=int(0)
rez1=int(0)
print(f'в диапазоне от 2 до {n} имеются следующие простые числа:')
for i in range (2,n+1):
    if n%i==0:
        rez_n+=1 #проверка введенного числа
    for j in range (1,n+1):
        if i%j==0: #проверка чисел в диапозоне
            rez1+=1
    if rez1==2:
        print(i)
        rez1=0
    if rez_n==2:
        print(f'Число {n} простое')
    else:
        print(f'Число {n} не простое')''' 

'''n=int(input('Введите число:'))
for x in range (1,n+1):
    rez=x%2
    if rez==0:
        print(f'{x}')'''
