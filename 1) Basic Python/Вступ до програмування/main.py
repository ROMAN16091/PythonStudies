"""
Цей скрипт демонструє основи роботи з різними типами даних у Python,
включаючи цілі та дійсні числа, рядки, булеві значення, операції з числами,
конвертацію типів, введення даних від користувача та логічні оператори.
"""

# Оголошення змінних цілочисельного типу
number1 = 5
number2 = 5
print(number1, number2)  # Виводимо значення обох змінних

# Робота з рядками та числами
str1 = "Hello"
str2 = "5"
print(number1 + number2)  # Додавання двох чисел
# print(number1 + str2)  # Помилка: неможливо додати число до рядка

# Отримання введення від користувача
name = input("Enter your name: ")
print(name)
print(type(name))  # Вивід типу введеного значення (завжди str)

# Конвертація введених даних у число
number3 = int(input('Enter number: '))
print(number3 + 5)  # Додаємо 5 до введеного числа
print(type(number3))  # Виводимо тип даних

print("Hello world")  # Виводимо рядок

# Конвертація чисел у різні системи числення
num_10 = 16
num_2 = bin(num_10)  # Двійкова система
num_8 = oct(num_10)  # Вісімкова система
num_16 = hex(num_10)  # Шістнадцяткова система
print(num_10)  # Вивід десяткового числа
print(num_2)  # Вивід двійкового представлення
print(num_8)  # Вивід вісімкового представлення
print(num_16)  # Вивід шістнадцяткового представлення

# Операції з числами (цілими та дійсними)
print(2.0 + 2)  # Додавання
print(2 - 2.0)  # Віднімання
print(2 * 2.0)  # Множення
print(2 / 2)  # Ділення
print(type(2 / 2))  # Тип даних після ділення

# Округлення та приведення до цілого
number4 = 2.999999
number5 = 2.0
print(int(number4))  # Обрізання дробової частини
print(int(number5))  # Перетворення дійсного числа в ціле

# Перетворення цілого числа у дійсне
number4 = 2
number5 = 2
print(float(number4))
print(float(number5))

# Булеві значення
bool_True = True
bool_False = False
print(bool_True)
print(bool_False)

# Порівняння чисел
print(5 < 5)  # Менше
print(5 > 5)  # Більше
print(5 <= 5)  # Менше або дорівнює
print(5 >= 5)  # Більше або дорівнює
print(5 == 5)  # Дорівнює
print(5 != 5)  # Не дорівнює

# Унарні операції
number6 = 5
print(-number6)  # Зміна знаку числа

# Піднесення до степеня
print(2**5)  # 2 в п'ятому степені

# Цілочисельне ділення та залишок
print(5 // 2)  # Ділення без залишку
print(5 % 2)  # Остача від ділення

# Обчислення кількості секунд у добі
s_per_m = 60  # Секунд у хвилині
m_per_h = 60  # Хвилин у годині
h_per_day = 24  # Годин у добі
result_task3 = s_per_m * m_per_h * h_per_day
print("Кількість секунд у добі:", result_task3)

# Обчислення кількості секунд у році
days_per_year1 = 365  # Звичайний рік
days_per_year2 = 366  # Високосний рік
result_task4_1 = days_per_year1 * result_task3
result_task4_2 = days_per_year2 * result_task3
print("Секунд у звичайному році:", result_task4_1)
print("Секунд у високосному році:", result_task4_2)

# Розрахунок секунд у році на новій планеті
name_new_planet = input("Введіть назву нової планети: ")
days_in_new_planet = int(input("Кількість днів у році на новій планеті: "))
result_task5 = days_in_new_planet * result_task3
print(f"На планеті {name_new_planet} {result_task5} секунд у році")

# Перевірка повноліття за місячним віком
monthly_age = int(input("Введіть ваш вік у місяцях: "))
year_age = monthly_age / 12
print(year_age > 18, "Вік у роках:", year_age)

monthly_age = int(input("Введіть ваш вік у місяцях: "))
year_age = monthly_age // 12  # Цілочисельне ділення
print(year_age >= 18, "Вік у роках:", year_age)
