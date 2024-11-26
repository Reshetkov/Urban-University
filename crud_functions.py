import sqlite3

db = sqlite3.connect("database.db")
cursor = db.cursor()


def initiate_db():
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL)
    ''')
    for i in range(1, 5):
        cursor.execute("INSERT INTO Products (id, title, description, price) VALUES(?, ?, ?, ?)",
                       (f'{i}', f'Продукт{i}', f'Описание{i}', f'{i * 100}'))
    db.commit()


def get_all_products():
    for i in range(1, 5):
        cursor.execute("SELECT id, title, description, price FROM Products")
    products = cursor.fetchall()
    db.commit()
    return products


initiate_db()
