import pandas as pd

# Создание словаря с данными о студентах
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Age': [20, 21, 19, 22, 20],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
    'GPA': [3.5, 3.2, 3.8, 3.6, 3.9]
}

# Создание DataFrame
df = pd.DataFrame(data)

# Вывод DataFrame
print(df)
# Вывод столбца 'Name' для всех студентов
names = df['Name']
print(names) 

# Выборка студентов женского пола
female_students = df[df['Gender'] == 'Female']

# Вывод информации о студентах женского пола
print(female_students)

# Нахождение индекса студента с наивысшим баллом GPA
index_max_gpa = df['GPA'].idxmax()

# Получение информации о студенте с наивысшим баллом GPA
student_max_gpa = df.loc[index_max_gpa]

# Вывод информации о студенте с наивысшим баллом GPA
print(student_max_gpa) 

# Увеличение возраста всех студентов на 1
df['Age'] = df['Age'] + 1


# Нахождение индекса студента с наименьшим возрастом
index_min_age = df['Age'].idxmin()

# Обновление балла GPA для студента с наименьшим возрастом
df.at[index_min_age, 'GPA'] = 4.0  # Предположим, что балл GPA для этого студента установлен в 4.0

# Вывод обновленного DataFrame
print(df)
# Вывод обновленного DataFrame
print(df)

# Данные о новом студенте
new_student_data = {'Name': 'Frank', 'Age': 23, 'Gender': 'Male', 'GPA': 3.7}

# Добавление нового студента в DataFrame
df = df.append(new_student_data, ignore_index=True)

# Вывод обновленного DataFrame
print(df)