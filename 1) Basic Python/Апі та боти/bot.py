# Крок 1. Імпорт бібліотек
import telebot  # Бібліотека для роботи з Telegram Bot API
import requests  # Бібліотека для виконання HTTP-запитів
from telebot import types  # Імпорт типів для створення кнопок і клавіатур
from telebot.types import BotCommand

# Крок 2. Налаштування API-ключів та ініціалізація бота
WEATHER_API_KEY = "5c62da02e9e30f91537def5669c10abc"  # Ключ для OpenWeatherMap API
TELEGRAM_BOT_TOKEN = ""  # Токен бота від BotFather
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)  # Створення екземпляру бота

# Устанавливаем команды
bot.set_my_commands([
    BotCommand("start", "Запуск бота"),
    BotCommand("help", "Помощь"),
    BotCommand("weather", "Узнать погоду"),
    BotCommand("joke", "Рассказать анекдот"),
    BotCommand("cat", "Прислать фото кота")
])

# Крок 3. Створення функції для відправлення меню (inline-клавіатури)
def send_menu(chat_id):
    """
    Функція відправляє повідомлення з inline-клавіатурою з кнопками:
    - Інформація (/info)
    - Погода (/weather)
    - Анекдот (/joke)
    - Кіт (/cat)
    Пояснення:
      - types.InlineKeyboardMarkup() створює об'єкт клавіатури.
      - types.InlineKeyboardButton() створює кнопку з текстом та callback_data.
      - markup.row() групує кнопки в один рядок.
      - bot.send_message() надсилає повідомлення з прикріпленою клавіатурою.
    """
    markup = types.InlineKeyboardMarkup()
    btn_info = types.InlineKeyboardButton("Інформація", callback_data="info")
    btn_weather = types.InlineKeyboardButton("Погода", callback_data="weather")
    btn_joke = types.InlineKeyboardButton("Анекдот", callback_data="joke")
    btn_cat = types.InlineKeyboardButton("Кіт", callback_data="cat")
    markup.row(btn_info, btn_weather)
    markup.row(btn_joke, btn_cat)
    bot.send_message(chat_id, "Оберіть опцію:", reply_markup=markup)


# Крок 4. Обробка команди /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    """
    Декоратор @bot.message_handler(commands=['start']) говорить, що ця функція викликається при отриманні команди /start.
    Функція:
      - Надсилає привітальне повідомлення.
      - Викликає send_menu() для показу меню.
    """
    welcome_text = (
        "Привіт! Я цікавий бот, який вміє:\n"
        "1. Розповідати про тебе (/info).\n"
        "2. Показувати погоду (/weather).\n"
        "3. Розповідати анекдоти (/joke).\n"
        "4. Надсилати випадкове фото кота (/cat).\n\n"
        "Обери опцію за допомогою кнопок нижче."
    )
    bot.send_message(message.chat.id, welcome_text)
    send_menu(message.chat.id)


# Крок 5. Обробка команди /info
@bot.message_handler(commands=['info'])
def handle_info(message):
    """
    Функція обробляє команду /info, надсилаючи інформацію про користувача:
      - ID, ім'я, username.
    Після цього викликається send_menu() для показу меню.
    """
    user = message.from_user
    info_text = f"👤 Інформація про користувача:\n"
    info_text += f"ID: {user.id}\n"
    info_text += f"Ім'я: {user.first_name}\n"
    info_text += f"Username: @{user.username}\n" if user.username else "Username: не вказаний\n"
    bot.send_message(message.chat.id, info_text)
    send_menu(message.chat.id)


# Крок 6. Обробка команди /weather та функція process_city_weather
@bot.message_handler(commands=['weather'])
def handle_weather(message):
    """
    Функція обробляє команду /weather:
      - Надсилає повідомлення з проханням ввести назву міста.
      - bot.register_next_step_handler() встановлює, що відповіддю на повідомлення буде викликана функція process_city_weather.
    """
    msg = bot.send_message(message.chat.id, "Введіть назву міста для отримання погоди:")
    bot.register_next_step_handler(msg, process_city_weather)


def process_city_weather(message):
    """
    Функція process_city_weather:
      - Отримує назву міста, введену користувачем.
      - Формує запит до OpenWeatherMap API.
      - Обробляє отримані дані та надсилає користувачу інформацію про погоду.
    """
    city = message.text.strip()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=uk"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            error_message = data.get("message", "Невідома помилка")
            bot.send_message(message.chat.id, f"Помилка: {error_message.capitalize()}")
            send_menu(message.chat.id)
            return

        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        weather_message = (
            f"🌤 Погода у місті {city.capitalize()}:\n"
            f"Температура: {temp}°C\n"
            f"Опис: {weather_desc}\n"
            f"Вологість: {humidity}%\n"
            f"Швидкість вітру: {wind_speed} м/с"
        )
        bot.send_message(message.chat.id, weather_message)
    except Exception as e:
        bot.send_message(message.chat.id, "Сталася помилка при отриманні даних про погоду.")
        print("Error fetching weather:", e)
    finally:
        send_menu(message.chat.id)


# Крок 7. Обробка команди /joke
@bot.message_handler(commands=['joke'])
def handle_joke(message):
    """
    Функція обробляє команду /joke:
      - Отримує випадковий анекдот через API.
      - Надсилає анекдот користувачу.
    """
    try:
        joke_response = requests.get("https://official-joke-api.appspot.com/random_joke")
        joke_data = joke_response.json()
        joke_text = f"{joke_data['setup']}\n{joke_data['punchline']}"
        bot.send_message(message.chat.id, joke_text)
    except Exception as e:
        bot.send_message(message.chat.id, "Не вдалося отримати анекдот. Спробуйте пізніше.")
        print("Error fetching joke:", e)
    finally:
        send_menu(message.chat.id)


# Крок 8. Обробка команди /cat
@bot.message_handler(commands=['cat'])
def handle_cat(message):
    """
    Функція обробляє команду /cat:
      - Отримує випадкове фото кота через API.
      - Надсилає фото користувачу.
    """
    try:
        cat_response = requests.get("https://api.thecatapi.com/v1/images/search")
        cat_data = cat_response.json()
        if cat_data:
            cat_image_url = cat_data[0].get("url")
            bot.send_photo(message.chat.id, cat_image_url)
        else:
            bot.send_message(message.chat.id, "Не вдалося отримати фото кота.")
    except Exception as e:
        bot.send_message(message.chat.id, "Сталася помилка при отриманні фото кота.")
        print("Error fetching cat image:", e)
    finally:
        send_menu(message.chat.id)


# Крок 9. Обробка callback-запитів для inline-кнопок
@bot.callback_query_handler(func=lambda call: call.data in ["info", "weather", "joke", "cat"])
def handle_callback(call):
    """
    Декоратор @bot.callback_query_handler з параметром:
      func=lambda call: call.data in ["info", "weather", "joke", "cat"]
    задає обробку callback-запитів (натискання на кнопки) для вказаних значень callback_data.

    Функція виконує:
      - info: надсилає інформацію про користувача.
      - weather: запитує назву міста для отримання погоди.
      - joke: надсилає випадковий анекдот.
      - cat: надсилає фото кота.

    Після кожної операції знову викликається send_menu() для показу меню.
    """
    chat_id = call.message.chat.id
    if call.data == "info":
        user = call.from_user
        info_text = f"👤 Інформація про користувача:\n"
        info_text += f"ID: {user.id}\n"
        info_text += f"Ім'я: {user.first_name}\n"
        info_text += f"Username: @{user.username}\n" if user.username else "Username: не вказаний\n"
        bot.send_message(chat_id, info_text)
        send_menu(chat_id)
    elif call.data == "weather":
        msg = bot.send_message(chat_id, "Введіть назву міста для отримання погоди:")
        bot.register_next_step_handler(msg, process_city_weather)
    elif call.data == "joke":
        try:
            joke_response = requests.get("https://official-joke-api.appspot.com/random_joke")
            joke_data = joke_response.json()
            joke_text = f"{joke_data['setup']}\n{joke_data['punchline']}"
            bot.send_message(chat_id, joke_text)
        except Exception as e:
            bot.send_message(chat_id, "Не вдалося отримати анекдот. Спробуйте пізніше.")
            print("Error fetching joke in callback:", e)
        finally:
            send_menu(chat_id)
    elif call.data == "cat":
        try:
            cat_response = requests.get("https://api.thecatapi.com/v1/images/search")
            cat_data = cat_response.json()
            if cat_data:
                cat_image_url = cat_data[0].get("url")
                bot.send_photo(chat_id, cat_image_url)
            else:
                bot.send_message(chat_id, "Не вдалося отримати фото кота.")
        except Exception as e:
            bot.send_message(chat_id, "Сталася помилка при отриманні фото кота.")
            print("Error fetching cat image in callback:", e)
        finally:
            send_menu(chat_id)


# Крок 10. Запуск бота за допомогою bot.polling

# bot.polling(none_stop=True) запускає безперервне опитування серверів Telegram,
# що дозволяє боту постійно отримувати нові повідомлення.
print("Бот запущено... Очікуємо повідомлень.")
bot.polling(none_stop=True)
