# ## Завдання 2. Генератор паролів
# 1. Генерація пароля:
#    - Реалізуйте функцію `generate_password(length, use_digits, use_symbols)`.  
#    - Для формування набору символів використовуйте списки та функцію `chr()`.
#      - Список літер формується з символів A–Z та a–z (за допомогою функції `range()`).  
#      - Якщо передбачено використання цифр, додайте символи від `'0'` до `'9'`.  
#      - Якщо дозволені спецсимволи, додайте, наприклад, символи з набору `!@#$%^&*()`.  
#    - Пароль генерується випадковим вибором символів із сформованого списку та повертається у вигляді рядка.
# 
# 2. Оцінка надійності пароля:  
#    - Функція `check_password_strength(password)` має оцінювати пароль за такими критеріями:
#      - Довжина: Пароль довжиною 8 і більше символів отримує максимальний бал за довжину, інакше – бал пропорційно.
#      - Унікальність: Відношення кількості унікальних символів до загальної довжини.
#      - Наявність цифр: Перевірка наявності хоча б однієї цифри.
#      - Наявність спецсимволів: Перевірка наявності хоча б одного символу з набору спецсимволів.
#    - Загальний бал обчислюється як середнє арифметичне зазначених показників і виводиться у відсотках.
# 
# 3. Робота з історією паролів:  
#    - Зберігайте згенеровані паролі у списку.  
#    - Реалізуйте функцію `find_strongest_password(passwords)`, яка перебирає історію та
#    знаходить пароль з максимальною оцінкою надійності.
# 
# 4. Інтерфейс:  
#    - Програма повинна працювати в циклі з меню, де доступні наступні опції:
#      - Генерація нового пароля (з запитом параметрів: довжина, використання цифр, спецсимволів).
#      - Перевірка надійності введеного користувачем пароля.
#      - Перегляд історії створених паролів із зазначенням їх надійності.
#      - Виведення найнадійнішого пароля з історії.
#      - Вихід із програми.
#
import random
def generate_password(lenght, use_digits, use_symbols):
    letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    digits = [chr(i) for i in range(48, 58)] if use_digits else []
    symbols = list("!@#$%^&*()") if use_symbols else []

    characters = letters + digits + symbols

    if not characters:
        print("Помилка: немає символів для генерації пароля.")
        return None

    password = "".join(random.sample(characters, lenght))
    return password

def check_password_strength(password):
    lenght_score = min(len(password)/8, 1)
    unique_chars_score = len(set(password)) / len(password)
    has_digits = any('0' <= char <= '9' for char in password)
    has_symbols = any(char in "!@#$%^&*()" for char in password)

    score = (lenght_score + unique_chars_score + has_digits + has_symbols) / 4

    return round(score * 100, 2)

def find_strongest_password(passwords):
    if not passwords:
        return None, 0
    scores = {pwd: check_password_strength(pwd) for pwd in passwords}
    strongest = max(scores, key=scores.get)
    return strongest, scores[strongest]


passwords = []
while True:
    print("\n1. Згенерувати новий пароль")
    print("2. Перевірити безпеку пароля")
    print("3. Переглянути історію паролів")
    print("4. Найнадійніший пароль")
    print("5. Вийти")

    choice = input("Оберить опцію: ")

    if choice == "1":
        length = int(input("Введіть довжину пароля: "))
        use_digits = input("Включати цири? (так/ні): ").strip().lower() == "так"
        use_symbols = input("Включати символи? (так/ні): ").strip().lower() == "так"

        new_password = generate_password(length, use_digits, use_symbols)

        if new_password:
            passwords.append(new_password)
            print(f"Password: {new_password}")

    elif choice == "2":
        password = input("Введіть пароль для перевірки: ")
        strength = check_password_strength(password)
        print(f"Надійність пароля: {strength}%")

    elif choice == "3":
        if passwords:
            print("Історія паролів: ")
            for pwd in passwords:
                print(f"{pwd} ({check_password_strength(pwd)}%)")
        else:
            print("Історія порожня. ")

    elif choice == "4":
        strongest, score = find_strongest_password(passwords)
        if strongest:
            print(f"Найнадійніший пароль: {strongest} ({score})")

    elif choice == "5":
        break

    else:
        print("Невідома команда, спробуйте ще раз. ")













