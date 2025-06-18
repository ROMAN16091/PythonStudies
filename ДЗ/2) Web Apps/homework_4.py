import mysql.connector as connector

conn = connector.connect(
    host="localhost",
    user="root",
    password="medved1603",
)

cursor = conn.cursor()

DB = 'users'
cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DB} DEFAULT CHARSET = utf8mb4')
conn.database = DB
cursor.close()
conn.close()

mydb = connector.connect(
    host="localhost",
    user="root",
    password="medved1603",
    database=DB
)

cur = mydb.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS users_data (
    id INT PRIMARY KEY AUTO_INCREMENT, 
    username VARCHAR(255) UNIQUE,                                 
    password VARCHAR(255),                         
    email VARCHAR(255) UNIQUE
)
''')


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def register(self):
        try:
            cur.execute('INSERT INTO users_data (username, password, email) VALUES (%s, %s, %s)',
                        (self.username, self.password, self.email))
            mydb.commit()
            print('Користувача зареєстровано!')
        except connector.IntegrityError as e:
            print(f'Помилка: {e}')

    @staticmethod
    def login(username, password):
        cur.execute('SELECT * FROM users_data WHERE username = %s AND password = %s', (username, password))
        res = cur.fetchone()
        return res is not None


cur.execute('''
CREATE TABLE IF NOT EXISTS accounts (
    site_name TEXT,
    login VARCHAR(255),
    password VARCHAR(255),
    login_type TEXT,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users_data(id)
)
''')


class Account:
    def __init__(self, site_name, login, password, login_type, user_id):
        self.site_name = site_name
        self.login = login
        self.password = password
        self.login_type = login_type
        self.user_id = user_id

    def add_account(self):
        cur.execute('SELECT * FROM accounts WHERE site_name = %s AND login = %s AND user_id = %s',
                    (self.site_name, self.login, self.user_id))
        if cur.fetchone():
            print('Цей акаунт вже існує на сайті!')
            return
        try:
            cur.execute('''
                INSERT INTO accounts (site_name, login, password, login_type, user_id) 
                VALUES (%s, %s, %s, %s, %s)
            ''', (self.site_name, self.login, self.password, self.login_type, self.user_id))
            mydb.commit()
            print('Аккаунт додано')
        except connector.IntegrityError:
            print('Помилка збереження аккаунта')

    @staticmethod
    def get_accounts_by_user(user_id):
        cur.execute('SELECT site_name, login FROM accounts WHERE user_id = %s', (user_id,))
        accounts = cur.fetchall()
        if not accounts:
            print('Аккаунти відсутні')
        else:
            print('Всі акаунти користувача:')
            for site, login in accounts:
                print(f'Сайт: {site}, Логін: {login}')

current_user_id = None
while True:
    print("\n--- Головне меню ---")
    print("1. Зареєструватися")
    print("2. Увійти")
    print("3. Додати аккаунт")
    print("4. Переглянути акаунти")
    print("5. Завершити роботу")
    choice = input("Виберіть опцію (1-5): ")

    match choice:
        case '1':
            username = input("Ім'я користувача: ")
            password = input("Пароль: ")
            email = input("Email: ")
            user = User(username, password, email)
            user.register()

        case '2':
            username = input("Ім'я користувача: ")
            password = input("Пароль: ")
            if User.login(username, password):
                cur.execute('SELECT id FROM users_data WHERE username = %s', (username,))
                current_user_id = cur.fetchone()[0]
                print("Вхід успішний!")
            else:
                print("Невірне ім'я користувача або пароль.")

        case '3':
            if current_user_id is None:
                print("Спочатку увійдіть.")
                continue
            site = input("Назва сайту: ")
            login_type = input("Тип входу (Google, Apple, Facebook, інше): ")
            if login_type.capitalize() in ['Google', 'Apple', 'Facebook']:
                login, password = None, None
            else:
                login = input("Логін: ")
                password = input("Пароль: ")
            acc = Account(site, login, password, login_type, current_user_id)
            acc.add_account()

        case '4':
            if current_user_id is None:
                print("Спочатку увійдіть до системи.")
                continue
            Account.get_accounts_by_user(current_user_id)

        case '5':
            print("До побачення!")
            break

cur.close()
mydb.close()
