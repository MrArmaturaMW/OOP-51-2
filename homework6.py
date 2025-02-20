import sqlite3

connect = sqlite3.connect('User.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()

def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен")

def get_user_by_name(name):
    cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
    user = cursor.fetchone()
    if user:
        return f"NAME: {user[0]} AGE: {user[1]} HOBBY: {user[2]}"
    else:
        return "Пользователь не найден"

add_user("John", 33, "плавание")

print(get_user_by_name("John"))
