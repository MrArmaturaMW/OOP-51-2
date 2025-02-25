import sqlite3

connect = sqlite3.connect('User.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
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

def get_all_users():
    cursor.execute('SELECT name, age, hobby FROM users')
    users = cursor.fetchall()
    print('Список всех пользователей')
    for i in users:
        print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")

def get_user_by_name(name):
    cursor.execute(
        'SELECT * FROM users WHERE name = ?',
        (name,)
    )
    user = cursor.fetchall()
    print(user)

def update_user(new_name, user_id):
    cursor.execute(
        'UPDATE users SET name = ? WHERE id = ?',
        (new_name, user_id)
    )
    connect.commit()
    print("User Updated!!")

def delete_user(row_id):
    cursor.execute(
        'DELETE from users WHERE rowid = ?',
        (row_id,)
    )
    connect.commit()
    print('User Deleted!!')

def update_grade(lesson_id, new_grade):
    cursor.execute(
        'UPDATE lessons SET grade = ? WHERE id = ?',
        (new_grade, lesson_id)
    )
    connect.commit()
    print("Subject ID updated!!")