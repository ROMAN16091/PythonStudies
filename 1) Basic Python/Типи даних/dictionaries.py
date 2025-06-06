# Робота зі словниками в Python

# Створення словників
my_dict1 = {"name": "Bob", "name1": "Bob"}  # Ключі повинні бути унікальні
print(my_dict1)

my_dict2 = {1: "one", 2: "two"}  # Ключі можуть бути різних типів
print(my_dict2)

# Вкладений словник
my_dict3 = {
    1: "one",
    "name": "two",
    "age": 23,
    "scores": {
        "Math": [80.5, 50],
        "English": 75
    }
}

my_dict4 = {"Hello": 123}  # Проста пара ключ-значення

# Отримання значень за ключем
# print(my_dict3[0])  # Викличе помилку, оскільки ключа 0 не існує
print(my_dict3["name"])
print(my_dict3["scores"]["Math"][0])  # Отримуємо оцінку з предмету "Math"

# Метод get() для безпечного отримання значення
print(my_dict3.get(1))  # Поверне "one"
print(my_dict3.get(0))  # Поверне None, оскільки ключа немає
print(my_dict3.get("name"))  # Поверне "two"

# Отримання списків ключів, значень та пар ключ-значення
print(list(my_dict3.items()))
print(list(my_dict3.keys()))
print(list(my_dict3.values()))

# Метод setdefault(): додає пару, якщо ключа немає
x = my_dict3.setdefault(0, 100)
print(x)  # Поверне 100
print(my_dict3)  # У словнику тепер є ключ 0

# Оновлення словника іншими даними
my_dict3.update(my_dict4)
print(my_dict3)

my_dict4.update(my_dict3)
print(my_dict4)

# Видалення елементів зі словника
x = my_dict3.pop("age")  # Видаляє ключ "age" і повертає його значення
print(x)
print(my_dict3)

# Видалення останнього елемента
try:
    x = my_dict3.pop("age123")  # Спроба видалити неіснуючий ключ викличе помилку
except KeyError:
    print("Ключ 'age123' не знайдено")

# Видаляємо останні елементи
while my_dict3:
    y = my_dict3.popitem()  # Видаляє останню пару ключ-значення
    print(y)
    print(my_dict3)
