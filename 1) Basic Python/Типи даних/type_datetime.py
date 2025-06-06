# Імпортуємо необхідні бібліотеки для роботи з часом
import time

# Фіксуємо початковий час
t1 = time.time()
# Затримуємо виконання програми на 5 секунд
time.sleep(5)
# Фіксуємо кінцевий час
t2 = time.time()
# Виводимо різницю між кінцевим і початковим часом (кількість секунд затримки)
print(t2 - t1)

# Другий спосіб імпортувати time для спрощення коду
from time import time, sleep
# Фіксуємо початковий час
t1 = time()
# Затримуємо виконання програми на 5 секунд
sleep(5)
# Фіксуємо кінцевий час
t2 = time()
# Виводимо різницю між кінцевим і початковим часом
print(t2 - t1)

# Імпортуємо бібліотеки для роботи з датами та часом
from datetime import datetime, timedelta

# Виводимо поточну дату та час
print(datetime.now())
# Виводимо конкретну дату та час
print(datetime(2000, 1, 28, 12, 25, 54))
# Виводимо тип різниці між двома датами
print(type(datetime.now()-datetime(2000, 1, 28)))
# Створюємо об'єкт timedelta для вказаної кількості днів і годин
print(timedelta(days=5000, hours=21))
# Виводимо дату, яка була на 366 днів раніше
print(datetime.now() - timedelta(days=366))

# Створюємо дату, яка була 7 днів тому, та виводимо різні її компоненти
date = datetime.now() - timedelta(days=7)
print(date.year)       # Виводимо рік
print(date.second)     # Виводимо секунди
print(date.minute)     # Виводимо хвилини
print(date.day)        # Виводимо день місяця

# Форматуємо поточну дату та час у різних форматах
print(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))  # день.місяць.рік година:хвилина:секунда
print(datetime.now().strftime("%d.%m.%y"))           # день.місяць.рік(останні 2 цифри)
print(datetime.now().strftime("%a"))                 # абревіатура дня тижня
print(datetime.now().strftime("%A"))                 # повна назва дня тижня
print(datetime.now().strftime("%w"))                 # номер дня тижня (0 - неділя, 6 - субота)
print(datetime.now().strftime("%b"))                 # абревіатура місяця
print(datetime.now().strftime("%B"))                 # повна назва місяця
print(datetime.now().strftime("%I%p"))               # година в 12-годинному форматі з AM/PM
print(datetime.now().strftime("%f"))                 # мікросекунди
print(datetime.now().strftime("%j"))                 # день року
print(datetime.now().strftime("%U"))                 # номер тижня (неділя на початку тижня)

# Перетворюємо рядок в дату та форматуючи його
date_str = "28/01/2025"
date_datetime = datetime.strptime(date_str, "%d/%m/%Y").strftime("%d.%m.%Y")
print(date_datetime)  # Виводимо дату у форматі день.місяць.рік

# Обчислюємо кількість секунд між двома датами та переводимо їх у роки
print((datetime.now() - datetime(2000, 5, 5)).total_seconds() / (60 * 60 * 24 * 365))

# Зміна максимальної кількості цифр, які можуть бути в рядку
import sys
sys.set_int_max_str_digits(1000000)

# Функція для обчислення ступеня 2
def power_2(n):
    return 2 ** n

# Фіксуємо час виконання функції для великого числа
t1 = time()
# Обчислюємо степінь 2 для числа 1000000
print(power_2(1000000))
t2 = time()
# Виводимо час виконання
print(t2 - t1)

# Фіксуємо час виконання функції для меншого числа
t1 = datetime.now()
print(power_2(100000))  # Обчислюємо степінь 2 для числа 100000
t2 = datetime.now()
# Виводимо кількість секунд та мікросекунд, що минули між початковим і кінцевим часом
print((t2 - t1).seconds)    # Кількість секунд
print((t2 - t1).microseconds)  # Кількість мікросекунд
