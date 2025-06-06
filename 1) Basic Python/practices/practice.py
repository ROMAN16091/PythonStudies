# Напишіть програму, яка аналізує введений користувачем рядок:
#
# Якщо рядок складається тільки з цифр, програма повинна вивести суму всіх цифр.
# Якщо рядок складається з букв, програма повинна вивести кількість голосних та приголосних букв.
# Якщо рядок містить і цифри, і букви, програма повинна вивести їх суму для цифр і кількість голосних/приголосних для букв.
while True:
    text = input("Введіть рядок або Enter для завершення: ").lower().strip()
    if text == '':
        print("Кінець програми".center(100, '-'))
        break

    try:
        if text.isdigit():
            sum_digits = sum(int(char) for char in text)
            print(f"Сума цифр: {sum_digits}")
        elif text.isalpha():
            vowels = "aeiou"
            consanants = "qwrtypsdfghjklzxcvbnm"
            vowels_count = sum(1 for char in text if char in vowels)
            consanants_count = sum(1 for char in text if char in consanants)
            print(f"Голосних: {vowels_count} Приголосних: {consanants_count}")
        elif text.isalnum():
            sum_digits = sum(int(char) for char in text if char.isdigit())
            vowels = "aeiou"
            consanants = "qwrtypsdfghjklzxcvbnm"
            vowels_count = sum(1 for char in text if char in vowels)
            consanants_count = sum(1 for char in text if char in consanants)
            print(f"Сума цифр: {sum_digits}")
            print(f"Голосних: {vowels_count} Приголосних: {consanants_count}")
    except Exception as ex:
        print(f"{ex}")
    finally:
        print("Спробуйте ввести інший рядок".center(100, '-'))

# Завдання
# 1.Запросіть у користувача ім'я та місячну зарплату в доларах та виведіть їхню річну зарплату в тисячах доларів.
# Наприклад: «Мішель», «12345» → «Річна зарплата Мішель складає 148 тис. доларів».
name = input()
salary = int(input())
salary_year = salary * 12
print(f'{name} {salary} ....')

# 2. Як вхідні дані візьмемо ціле число; Це буде ціле число від 101 до 999, а його остання цифра
# не дорівнює нулю(робити перевірку не обовʼязково) Виведіть число, що складається
# з чисел першого у зворотньому порядку.
# Наприклад: 256 → 652.
import random
num1 = random.randint(101, 999)
print(num1)
num1 = int(str(num1)[::-1])
print(num1)
num1_1 = num1 % 10
print(num1_1)
num1_2 = (num1 % 100) // 10
print(num1_2)
num1_3 = num1 // 100
print(num1_3)
result = num1_1 * 100 + num1_2 * 10 + num1_3
print(result)


# Напишіть програму, яка запитує в користувача ціле число та генерує таблицю множення для цього числа,
# використовуючи цикл for з range.
#
# Програма повинна вивести таблицю множення від 1 до 10 для введеного числа.
# Після цього програма повинна попросити користувача ввести діапазон чисел (наприклад, від 1 до 5) і
# вивести таблицю множення для введеного числа в цьому діапазоні.
# Програма повинна перевіряти правильність введеного діапазону (введення повинно бути цілим числом і
# правильний порядок: початок діапазону менше кінця).
while True:
    try:
        # Запитуємо число для таблиці множення
        number = int(input("Enter number: "))
        print(f"Таблиця множення для числа {number} від 1 до 10")
        for i in range(1,11):
            print(f"{number} * {i} = {number*i}")

        # Запитуємо діапазон для таблиці
        start = int(input("Enter start: "))
        end = int(input("Enter end: "))

        if start > end:
            print("Помилка: початок діапазону має бути меньшим за кінець")
        else:
            print(f"Таблиця множення для числа {number} від {start} до {end}")
            for i in range(start, end + 1):
                print(f"{number} * {i} = {number * i}")
    except Exception as ex:
        print(f"Error {ex}")

    exit_choce = input("Бажаєте вийти? (yes/no)").lower().strip()
    if exit_choce == 'yes':
        print("End")
        break


# Напишіть програму, яка:
#
# Генерує випадкове число від 1 до 100 (за допомогою random.randint).
# Просить користувача вгадати число, підказуючи, більше чи менше введене число за загаданим.
# Продовжує запитувати числа, поки користувач не вгадає.
# Після вгадування виводить кількість спроб.
import random

secret_number = random.randint(1,10000)
attempts = 0
print("Я загадав число від 1 до 10000. Спробуй вгадати")

while True:
    try:
        user_number = int(input("Введіть ваше число: "))
        attempts += 1
        if user_number < secret_number:
            print("Загадане число більше")
        elif user_number > secret_number:
            print("Загадане число меньше")
        else:
            print(f"Ви вгадали число {secret_number} за {attempts} спроб")
            break

    except Exception as ex:
        print(f"Error {ex}")

# Напишіть програму, яка:
#
# Генерує випадковий рядок з літер (маленькі й великі) і цифр довжиною N, де N вводить користувач.
# Виводить цей рядок.
# Аналізує його:
# Кількість великих і маленьких літер.
# Кількість цифр.
# N = 10
# str1 = "qwertyuioppasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789"
# random_str = "".join(random.choice(str1) for _ in range(N))
# print(random_str)
#
# Напишіть програму, яка:
#
# Запитує у користувача рядок.
# Видаляє всі розділові знаки та перетворює текст у нижній регістр.
# Аналізує слова у тексті:
# Виводить 5 найпоширеніших слів.
# Виводить середню довжину слів у тексті.
# Визначає, чи є в тексті паліндроми (слова, що читаються однаково з обох боків, наприклад, "око", "ротор").

# Запитуємо тукст у користувача і перетворюємо текст у нижній регістр
text = input("Enter text: ").lower()
clean_text = ""
print(ord('a'))
print(chr(97))
for char in text:
    if 'a' <= char <= 'z' or char == " ":
        clean_text += char

words = clean_text.split()

unique_words = []
word_count = []

# words = ['process', 'finished', 'process', 'with', 'exit', 'code']
# unique_words = []
# word_count = []
for word in words:
    # 1 iteration -> word = 'process'
    # 'process' in unique_words -> False -> else
    # 2 iteration -> word = 'finished'
    # 'finished' in unique_words -> False -> else
    # 3 iteration -> word = 'process'
    # 'process' in unique_words -> True -> if
    if word in unique_words:
        #  3 iteration -> word = 'process'
        # unique_words.index(word) -> unique_words.index('process') -> 0
        # word_count[unique_words.index(word)] -> word_count[0] += 1 -> word_count = [2, 1]
        word_count[unique_words.index(word)] += 1
    else:
        unique_words.append(word) # 1 iteration -> unique_words = ['process']
                                # 2 iteration -> unique_words = ['process', 'finished']
        word_count.append(1) # word_count = [1, 1]

print(unique_words)
print(word_count)

word_count = [3, 1, 2, 2, 4]
# range(len(word_count)) -> range(5) -> i = 0, 1, 2, 3, 4
for i in range(len(word_count)):
    for j in range(i+1, len(word_count)): # range(1, 5), range(2, 5), range(3, 5), range(4, 5), range(5, 5)
        # [3, 1, 2, 2, 4]
        # 1 iter -> 3 < 1 -> [3, 1, 2, 2, 4]
        # 2 iter -> 3 < 2 -> [3, 1, 2, 2, 4]
        # 3 iter -> 3 < 2 -> [3, 1, 2, 2, 4]
        # 4 iter -> 3 < 4 -> [4, 1, 2, 2, 3]
        # 5 iter -> 1 < 2 -> [4, 2, 1, 2, 3]
        # 6 iter -> 2 < 2 -> [4, 2, 1, 2, 3]
        # 7 iter -> 2 < 3 -> [4, 3, 1, 2, 2]
        # 8 iter -> 1 < 2 -> [4, 3, 2, 1, 2]
        # 9 iter -> 2 < 2 -> [4, 3, 2, 1, 2]
        # 10 iter -> 1 < 2 -> [4, 3, 2, 2, 1]
        if word_count[i] < word_count[j]:
            word_count[i], word_count[j] = word_count[j], word_count[i]
            unique_words[i], unique_words[j] = unique_words[j], unique_words[i]
print(unique_words)
print(word_count)



print(f"5 найпоширеніших слів: {unique_words[:5]}")

# words = ['process', 'finished', 'process', 'with', 'exit', 'code']
# words = []
if words: #len(words) != 0
                   #sum([7, 8, 7, 4, 4, 4]) = 34
    total_len = sum(len(word) for word in words)
            #  34 / 6 = 5.666666
    avg_len = total_len / len(words)
else:
    avg_len = 0

print(f"Середня довжина слова: {avg_len:.2f}")

palindromes = []
for word in unique_words:
    if word == word[::-1] and len(word) > 1:
        palindromes.append(word)

print(f"Паліндроми у тексті: {palindromes}")



# Напишіть програму, яка симулює казино-рулетку:
#
# Генерує випадкове число від 0 до 36 (random.randint(0, 36)).
# Запитує у користувача ставку:
# Чи ставить він на конкретне число або на колір (червоне/чорне).
# Користувач вводить число або колір.
# Програма визначає результат:
# Якщо користувач вгадав число — він отримує x35 від ставки.
# Якщо користувач вгадав колір — отримує x2 від ставки.
# Якщо не вгадав — програє.
# Програма працює в циклі, поки користувач не введе "вихід".

import random

balance = 1000

while True:
    print(f"Ваш баланс: {balance}".center(100, '-'))

    bet_type = input("Ставка (число 0-36 або колір червоне/чорне/зелений, або вихід): ").lower().strip()

    if bet_type == "вихід":
        print(f"Гра завершена. Ваш баланс: {balance}")
        break

    amount = int(input("Введіть суму ставки: "))

    if amount > balance or amount <= 0:
        print("Недостатньо коштів або некоректна ставка!")
        continue

    result = random.randint(0, 36)

    if result == 0:
        result_color = "зелений"
    elif result % 2 == 0:
        result_color = "чорне"
    else:
        result_color = "червоне"

    print(f"Випало: {result} - {result_color}")

    if bet_type.isdigit() and int(bet_type) == result:
        balance += amount * 35
        print(f"Ви вгалали число ваш виграш х35 ({amount * 35})")
    elif bet_type == "червоне" and result_color == "червоне":
        balance += amount * 2
        print(f"Ви вгалали колір ваш виграш х2 ({amount * 2})")
    elif bet_type == "чорне" and result_color == "чорне":
        balance += amount * 2
        print(f"Ви вгалали колір ваш виграш х2 ({amount * 2})")
    elif bet_type == "зелений" and result_color == "зелений":
        balance += amount * 70
        print(f"Ви вгалали зелений колір ваш виграш х70 ({amount * 70})")
    else:
        balance -= amount
        print(f"Ви програли ({amount})")

    if balance <= 0:
        print("У вас закінчилися гроші! Гра завершена")
        break