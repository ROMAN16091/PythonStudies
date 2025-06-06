# Головний файл для демонстрації роботи об'єктно-орієнтованого програмування

import car
from car import Car

# Створюємо об'єкт автомобіля
car1 = Car("Audi", 2022)
print(car1.start())
print(car1.stop())

# Імпортуємо класи фігур і створюємо об'єкти
from shape import Rectangle, Circle

rect = Rectangle(10, 10)
circle = Circle(5)
print(rect.area())  # Виведе 100
print(circle.area())  # Виведе 78.5

# Імпортуємо клас Point і демонструємо операції над точками
from point import Point
p1 = Point(5, 5)
p2 = Point(10, 1)
p3 = Point(20, 20)

print((p1 + p2 + p3).x)  # Координата x після додавання
print((p1 + p2 + p3).y)  # Координата y після додавання
print((p1 - p2).x)  # Координата x після віднімання
print((p1 - p2).y)  # Координата y після віднімання
print(p1)  # Вивід об'єкта p1
print(p1 + p2 + p3 - p2)  # Комплексна операція

str1 = f'Result p1 + p2 {p1 + p2}'
print(str1)
print(-p1)  # Унарний мінус
print(p1 == p2)  # Перевірка на рівність
print(p1 != p2)  # Перевірка на нерівність
print(p1 > p2)  # Перевірка p1 > p2
print(p2 > p1)  # Перевірка p2 > p1