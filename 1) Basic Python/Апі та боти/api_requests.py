
#HTTP-методи
# GET - отримання даних з сервера (отримання інформації про пивоварню або пост)
# POST - створює новий ресурс (створоння нового запису (поста))
# PUT - Оновлення існуючего ресурсу
# DELETE - Видалення ресурсу

#HTTP-статус коди
# 200 OK Запит виконано успішно, дані отримано
# 201 Created Ресурс створено успішно
# 400 Bad Request Неправильний запит, сервер не може його обробити
# 401 Unautorized Проблема з авторизацією
# 404 Not Found Ресурс не знайдено
# 500 Internal Server Error Помилка на стороні сервера
#
# import requests
#
# url = "https://jsonplaceholder.typicode.com/posts"
# params = {"userId": 2}
#
# response = requests.get(url, params=params)
# if response.status_code == 200:
#     data = response.json()
#     for post in data:
#         print(f"ID: {post['id']}, Title: {post['title']}\nBody: {post['body']}\n")
#
# else:
#     print(f"Error {response.status_code}")
#
# url_erorr = "https://jsonplaceholder.typicode.com/error"
#
# try:
#     response = requests.get(url_erorr)
#     response.raise_for_status()
#     print(response.json())
# except requests.exceptions.RequestException as ex:
#     print(f"Error {ex}")

import requests
import json
import datetime

session = requests.Session()
base_url = "https://api.openbrewerydb.org/breweries/"

def get_brew_by_city(city: str):
    params = {"by_city": city}
    try:
        response = session.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as ex:
        print(f"Error {ex}")
        return None

def get_brew_by_type(brew_type: str):
    params = {"by_type": brew_type}
    try:
        response = session.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as ex:
        print(f"Error {ex}")
        return None

def get_brew_details(brew_id: str):
    url_details = base_url + brew_id
    try:
        response = session.get(url_details)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as ex:
        print(f"Error {ex}")
        return None


def save_history(query_type, query_details, results):
    with open("../history.txt", "a", encoding="windows-1251") as file:
        timestamp = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        history_record = {
            "timestamp": timestamp,
            "query_type": query_type,
            "query_details": query_details,
            "results": results
        }
        file.write(json.dumps(history_record, indent=2))
        file.write('-' * 75)
        file.write('\n')

def show_history():
    try:
        with open("../history.txt", "r", encoding="windows-1251") as file:
            content = file.read()
            if content.strip() == "":
                print("Історія запитів порожня")
            else:
                print(content)
    except FileNotFoundError:
        print("Історія запитів порожня")

def print_brew_list(brews):
    if not brews:
        print("Пивоварень не знайдено")
        return

    for b in brews:
        print(f"ID: {b.get('id')}")
        print(f"Країна: {b.get('country')}")
        print(f"Місто: {b.get('city')}")
        print(f"Назва: {b.get('name')}")
        print(f"Тип: {b.get('brewery_type')}")
        print('-' * 50)

while True:
    print("1. Пошук за містом")
    print("2. Пошук за типом")
    print("3. Перегляд деталей")
    print("4. Історія")
    print("5. Вихід")

    choice = input("Оберіть опцію (1-5): ")

    if choice == "1":
        city = input("Введіть назву міста: ")
        brews = get_brew_by_city(city)
        if brews is not None:
            print_brew_list(brews)
            save_history("Пошук за містом", city, brews)

    elif choice == "2":
        array_types = ["micro", "nano", "regional", "brewpub", "large", "planning", "bar", "contract", "proprietor", "closed"]
        prompt_type = "Введіть тип пивоварні\n" + ", ".join(array_types) + ": "
        brew_type = input(prompt_type)
        brews = get_brew_by_type(brew_type)
        if brews is not None:
            print_brew_list(brews)
            save_history("Пошук за типом", brew_type, brews)

    elif choice == "3":
        brew_id = input("Введіть id: ")
        details = get_brew_details(brew_id)
        if details is not None:
            print(json.dumps(details, indent=2))
            save_history("Перегляд деталей", brew_id, details)

    elif choice == "4":
        show_history()

    elif choice == "5":
        break

    else:
        print("Невірний вибір операції")

with open("test.txt", "w") as file:
    file.write("Невірний вибір операції")