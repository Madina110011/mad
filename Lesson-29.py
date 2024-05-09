import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')
cursor.execute('''
    INSERT INTO Students (name, age)
    VALUES (?, ?)
''', ('Alice', 25))
cursor.execute('''
    INSERT INTO Students (name, age)
    VALUES (?, ?)
''', ('Bob', 30))
cursor.execute('SELECT * FROM Students')
students = cursor.fetchall()
print("Список студентов:")
for student in students:
    print(student)

cursor.execute('''
    UPDATE Students
    SET age = ?
    WHERE name = ?
''', (28, 'Alice'))

cursor.execute('''
    DELETE FROM Students
    WHERE name = ?
''', ('Bob',))

conn.commit()
cursor.close()
conn.close()