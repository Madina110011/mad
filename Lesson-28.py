import sqlite3
conn = sqlite3.connect('transactions.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Transactions (
        id INTEGER PRIMARY KEY,
        description TEXT,
        amount REAL
    )
''')
def add_transaction(description, amount):
    cursor.execute('''
        INSERT INTO Transactions (description, amount)
        VALUES (?, ?)
    ''', (description, amount))
    conn.commit()

add_transaction("Покупка продуктов", 50.0)
add_transaction("Оплата счетов", 100.0)
cursor.close()
conn.close()


