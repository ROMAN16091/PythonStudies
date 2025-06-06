import sqlite3, re  # Імпортуємо модулі для роботи з базою даних (sqlite3) і регулярними виразами (re)

# Підключення до бази даних (якщо файлу немає — створюється)
conn = sqlite3.connect('my_database.db')

# Створення "курсорa" — інструменту для виконання SQL-запитів
cur = conn.cursor()

# Створюємо таблицю "users", якщо її ще немає
cur.execute('''
CREATE TABLE IF NOT EXISTS users
(
    id    INTEGER PRIMARY KEY AUTOINCREMENT,  -- Унікальний ID користувача (збільшується автоматично)
    name  TEXT,                                -- Ім'я користувача
    age   INTEGER,                             -- Вік
    email TEXT UNIQUE                          -- Email (має бути унікальним)
)
''')

# Додаємо одного користувача
cur.execute('INSERT INTO users (name, age, email) VALUES (?, ?, ?)', ('Ivan', 30, 'ivan@example.com'))

# Додаємо кількох користувачів одразу
users = [
    ('Bob', 25, 'bob@example.com'),
    ('Alice', 28, 'alice@example.com')
]
cur.executemany('INSERT INTO users (name,age, email) VALUES (?,?,?)', users)

# Оновлюємо вік користувача з ім’ям 'IVAN' (але в БД ім’я записане як 'Ivan', тож це не спрацює)
cur.execute('UPDATE users SET age = ? WHERE name = ?', (31, 'IVAN'))

# Видаляємо всіх користувачів, чий вік менше 26 років
cur.execute('DELETE FROM users WHERE age < ?', (26,))

# Зберігаємо зміни в базі даних
conn.commit()

# Вибираємо всі записи з таблиці "users"
cur.execute('SELECT * FROM users')

# Завантажуємо всі результати в змінну rows
rows = cur.fetchall()
for row in rows:
    print(row)  # Виводимо кожен рядок (користувача)

# Спроба ще раз зчитати дані після fetchall() — нічого не отримаємо (порожньо)
user1 = cur.fetchone()
user2 = cur.fetchone()
user3 = cur.fetchone()
print(user1)
print(user2)
print(user3)

# Додаємо ще двох користувачів
users = [
    ('Ira', 23, 'ira@example.com'),
    ('Igor', 22, 'igor@example.com')
]
cur.executemany('INSERT INTO users (name,age, email) VALUES (?,?,?)', users)

# Ще раз зберігаємо зміни в базі
conn.commit()

# --- Нижче спроба вибірки по імені через REGEXP (регулярний вираз) ---

# Функція для підтримки REGEXP у SQLite (бо за замовчуванням не працює)
def regexp(pattern, string):
    return re.search(pattern, string) is not None

# Реєструємо функцію regexp як SQL-функцію REGEXP
conn.create_function('REGEXP', 2, regexp)

# Вибираємо користувачів, чиє ім’я починається на "B" (з великої літери)
cur.execute('SELECT * FROM users WHERE name REGEXP ?', ('^B',))
users_I = cur.fetchall()

# Помилка: тут виводяться не результати запиту, а старий список users
for user in users:
    print(user)

# Закриваємо курсор і з'єднання з базою
cur.close()
conn.close()
