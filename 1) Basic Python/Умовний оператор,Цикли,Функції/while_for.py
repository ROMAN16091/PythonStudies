import random

# Перший цикл
num = 0
while num < 10:
    print(num)
    num += 1

# Другий цикл
num = 10
while True:
    if num == 0:
        break
    if num == 2 or num == 5:
        num -= 1
        continue
    else:
        print(num)
        num -= 1

# Гра для перевірки математичних операцій
exit_yes_no = "no"
count = 0
count_correct = 0
while True:
    if exit_yes_no == "yes":
        break
    try:
        number1 = random.randint(1, 10)
        number2 = random.randint(1, 10)
        user_answer = int(input(f"{number1} + {number2} = "))
        count += 1
        correct_answer = number1 + number2
        if user_answer == correct_answer:
            print("Yes")
            count_correct += 1
        else:
            print(f"No {correct_answer}")

        if count % 5 == 0:
            exit_yes_no = input("Exit (yes/no): ").lower()

    except Exception as ex:
        print(f"Error: {ex}")
        exit_yes_no = input("Exit (yes/no): ").lower()

    finally:
        print(f'{count_correct}/{count} - {(count_correct/count)*100}%')

# Виведення чисел із рядка
str1 = "123456789"
for i in str1:
    if i == '1':
        print(10)
    elif i == '5':
        print(50)
    else:
        print(i)

# Виведення URL кілька разів
for _ in range(1, 10):
    print("http://google.com")


# Напишіть програму, яка аналізує введений користувачем рядок:
#
# Якщо рядок складається тільки з цифр, програма повинна вивести суму всіх цифр.
# Якщо рядок складається з букв, програма повинна вивести кількість голосних та приголосних букв.
# Якщо рядок містить і цифри, і букви, програма повинна вивести їх суму для цифр і кількість голосних/приголосних для букв.

# Програма для аналізу рядка
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
        elif any(char.isdigit() for char in text) and any(char.isalpha() for char in text):
            sum_digits = sum(int(char) for char in text if char.isdigit())
            vowels = "aeiou"
            consanants = "qwrtypsdfghjklzxcvbnm"
            vowels_count = sum(1 for char in text if char in vowels)
            consanants_count = sum(1 for char in text if char in consanants)
            print(f"Сума цифр: {sum_digits}")
            print(f"Голосних: {vowels_count} Приголосних: {consanants_count}")
    except Exception as ex:
        print(f"Error: {ex}")
    finally:
        print("Спробуйте ввести інший рядок".center(100, '-'))