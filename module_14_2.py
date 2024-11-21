import sqlite3

db = sqlite3.connect("not_telegram.db")
cursor = db.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''')

for i in range(1, 11, 1):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)",
                   (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', '1000'))

for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i}"))

for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i}",))
    cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
cursor.execute("SELECT COUNT (*) FROM Users")
total_1 = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
total_2 = cursor.fetchone()[0]

print(total_2 / total_1)

db.commit()
db.close()
