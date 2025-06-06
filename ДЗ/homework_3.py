import sqlite3
conn = sqlite3.connect('my_database.db')

cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS users
(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT UNIQUE,                                
    password TEXT,                         
    email TEXT UNIQUE                          
)
''')

conn.commit()


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


    def register(self):
        try:
            cur.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)', (self.username, self.password, self.email))
            conn.commit()
            print('Користувача зареєстровано!')
        except sqlite3.IntegrityError:
            print('Користувач вже існує!')


    @staticmethod
    def login(username, password):
        cur.execute('SELECT * FROM users WHERE (username = ? AND password = ?)', (username, password))
        res = cur.fetchone()
        return res is not None


# user = User('Ivan', 123, 'ivan@gmail.com')
# user.register()
# print(user.login('Ivan', 123))







while True:
    print('Виберіть операцію:\n1 - Зареєструватися\n2 - Увійти\n3 - Вийти')
    oper = input()
    match oper:
        case '1':
            username = input("Введіть ім'я: ").strip()
            password = input('Введіть пароль: ').strip()
            email = input('Введіть електронну адресу: ').strip()
            user = User(username,password,email)
            user.register()
        case '2':
            username = input("Введіть ім'я: ").strip()
            password = input('Введіть пароль: ').strip()
            if User.login(username, password):
                print('Успішний вхід!')
            else:
                print('Неправильні дані!')
        case '3':
            print('Роботу завершено.')
            break



