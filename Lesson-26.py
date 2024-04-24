'''import sqlite3
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS my_table (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER
                )''')
data_to_insert = [
    ('Alice', 30),
    ('Bob', 25),
    ('Charlie', 35)
]
cursor.executemany('''INSERT INTO my_table (name, age) VALUES (?, ?)''', data_to_insert)
conn.commit()
conn.close() '''

import sqlite3
import cvs

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute('''
   CREATE TABLE IF NOT EXISTS Employees (
       EmployeesID INTEGER PRIMARY KEY,
       FirstName TEXT,
       lastName TEXT,
       BirthDate DATE, 
       DepartmentID INTEGER
    );
''')

with open('/path/to/datafile.csv', 'r') as csvfile:
   cvsreader = cvs.reader(cvsfile)
   next(csvreader)
   cursor.executemany('INSERT INTO Employees VALUES (?, ?, ?, ?, ?);', csvreader)
   conn.commit()
   conn.close()