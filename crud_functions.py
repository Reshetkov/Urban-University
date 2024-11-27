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
#    for i in range(1, 5):
#        cursor.execute("INSERT INTO Products (id, title, description, price) VALUES(?, ?, ?, ?)",
#                           (f'{i}', f'Продукт{i}', f'Описание{i}', f'{i * 100}'))

    cursor.execute(''' CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL)
    ''')
    db.commit()


def get_all_products():
    for i in range(1, 5):
        cursor.execute("SELECT id, title, description, price FROM Products")
    products = cursor.fetchall()
    db.commit()
    return products


def add_user(username, email, age):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)",
                   (username, email, age, '1000'))
    db.commit()


def is_included(username):
    cursor.execute("SELECT username FROM Users")
    users = cursor.fetchall()
    is_on_the_list = any(user[0] == username for user in users)
    return is_on_the_list


initiate_db()
