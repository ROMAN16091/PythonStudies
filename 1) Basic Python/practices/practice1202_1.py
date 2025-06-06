# ## Завдання 1. Система бронювання номерів
#  
# 1. Зберігання інформації про номери:  
#    - Використовуйте словник (dict), де ключ – номер кімнати (число від 101 до 110), а значення – кортеж з типом кімнати
#       та ціною за ніч.
#    - Типи номерів можуть бути, наприклад, `"Економ"`, `"Стандарт"`, `"Люкс"`, а ціни задаються через допоміжний словник.
# 
# 2. Бронювання:  
#    - Заброньовані номери повинні зберігатися у множині (set).  
#    - При бронюванні програма повинна перевіряти, чи введений номер існує та чи він ще не заброньований.  
#    - При відміні бронювання перевірте, чи номер дійсно заброньовано.
# 
# 3. Функціональність:  
#    - Функція `generate_rooms()` – для генерації словника з номерами та їх характеристиками.  
#    - Функція `show_available_rooms()` – для виведення на екран списку номерів, які ще доступні (не заброньовані).  
#    - Функція `book_room()` – для бронювання вибраного номера.  
#    - Функція `cancel_booking()` – для відміни бронювання.  
#    - Функція `save_bookings()` – для запису заброньованих номерів у текстовий файл (по одному номеру в рядок).
# 
# 4. Інтерфейс:  
#    - Програма повинна працювати в циклі, пропонуючи користувачу вибір дій (наприклад, меню з пунктами: показати доступні
#       номери, забронювати, відмінити бронювання, зберегти, вийти).
#    - Виводити повідомлення про успішне або невдале виконання операцій.

import random

def generate_rooms():
    room_types = ["Економ", "Стандарт", "Люкс"]
    prices = {"Економ": 500, "Стандарт": 1000, "Люкс": 2000}
    rooms = {}
    for room in range(101, 111):
        r_type = random.choice(room_types)
        r_price = prices[r_type]
        rooms[room] = (r_type, r_price)

    return rooms

def show_available_rooms(rooms, booked):
    print("\nДоступні номери:")
    for room, details in rooms.items():
        if room not in booked:
            print(f"Номер {room}: {details[0]} - {details[1]}$")

def book_room(rooms, booked):
    room_number = int(input("Введіть номер кімнати для бронювання: "))
    if room_number in rooms and room_number not in booked:
        booked.add(room_number)
        print(f"Кімнату {room_number} заброньовано!")
    else:
        print("Кімната не існує або вже заброньована.")

def cancel_booking(booked):
    room_number = int(input("Введіть номер кімнати для відміни бронювання: "))
    if room_number in booked:
        booked.remove(room_number)
        print(f"Бронювання кімнати {room_number} скасовано")
    else:
        print("Ця кімната не була заброньована")

def save_booking(booked, filename="booking.txt"):
    with open(filename, "w") as file:
        for room in booked:
            file.write(f"{room}\n")
    print("Бронювання збережено у файл")



booked = set()
rooms = generate_rooms()
while True:
    print("\n1. Показати доступні номери")
    print("2. Забронювати номер")
    print("3. Переглянути заброньовані номери")
    print("4. Відмінити бронювання")
    print("5. Зберегти бронювання у файл")
    print("6. Вийти")

    choice = input("Оберить операцію: ")

    if choice == "1":
        show_available_rooms(rooms, booked)
    elif choice == "2":
        book_room(rooms, booked)
    elif choice == "3":
        print(f"Заброньовані номери: {booked}")
    elif choice == "4":
        cancel_booking(booked)
    elif choice == "5":
        save_booking(booked)
    elif choice == "6":
        print("До побачення!")
        break
    else:
        print("Невідома команда, спробуйте ще раз.")






