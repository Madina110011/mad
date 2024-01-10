'''name=("Madina")
age=("25")
text= "My name is {} and I am {}.".format(name,age)
print(text)
message=f"Hi, {name}! Are you {age}?"
print(message) 

a=int(input('Введите оценку:'))
b=int(input('Введите оценку:'))
c=int(input('Введите оценку:'))
sr=(a+b+c)/3
print('Средний балл:',sr)''' 

'''m_a=int(input('Введите оценку по математике'))
m_b=int(input('Введите оценку по математике'))
m_c=int(input('Введите оценку по математике'))
h_a=int(input('Введите оценку по химие'))
h_b=int(input('Введите оценку по химие'))
h_c=int(input('Введите оценку по химие'))
f_a=int(input('Введите оценку по физике'))
f_b=int(input('Введите оценку по физике'))
f_c=int(input('Введите оценку по физике'))
m_sr=(m_a+m_b+m_c)/3
h_sr=(h_a+h_b+h_c)/3
f_sr=(f_a+f_b+f_c)/3
sr=(m_sr+h_sr+f_sr)/3
print(f'Средний балл по математике:{m_sr:.2f}')
print(f'Средний балл по математике:{h_sr:.2f}')
print(f'Средний балл по математике:{f_sr:.2f}')
print(f'Средний балл по предметам:{sr:.2f}')'''

name=input('Как Вас зовут?')
age=input('Ваш возраст:')
iin=input('Введите ИИН:')
if iin.isdigit()==False:
    iin='Некорректный ИИН'
adr=input('Введите адрес проживания:')
print(f'Личные данные ученика {name}')
#print(f'Имя: {name}',sep='\n', 'Возраст: {age}',sep='\n','ИИН: {inn}', sep='\n','Адрес:{adr}')
print('Имя:',name)
print('Возраст:',age)
print('ИИН:',iin)
print('Адрес',adr)