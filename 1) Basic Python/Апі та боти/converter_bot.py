# https://t.me/converter10_bot
import telebot, requests, json
from telebot import types
from telebot.types import BotCommand


def save_conversation_request(request_data):
    try:
        with open('history_data.json', 'r') as file:
            history = json.load(file)
    except Exception as ex:
        history = []
        print(ex)
    history.append(request_data)
    history = history[-10:]
    with open('history_data.json', 'w') as file:
        print(history)
        json.dump(history, file, indent=4)


user_data = {}
url = requests.get('https://api.monobank.ua/bank/currency')
data = url.json()
TELEGRAM_TOKEN_BOT = '7775207380:AAFMoZfmJmeW-Q0NsrQGApp5BdRMzK1NUtg'
bot = telebot.TeleBot(TELEGRAM_TOKEN_BOT)
bot.set_my_commands([
    BotCommand('start', 'Запуск бота'),
    BotCommand('rate', 'Поточний курс валют'),
    BotCommand('convert', 'Почати конвертацію')
])


@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Допомога", callback_data="help")
    markup.add(btn1)
    bot.send_message(message.chat.id, f"Привіт {message.from_user.first_name}, я бот - конвертер валют",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "help")
def handle_help_callback(call):
    bot.answer_callback_query(callback_query_id=call.id, text="Список команд надіслано!")
    send_help(call.message.chat.id)


def send_help(chat_id):
    help_message = """
            Доступні команди
        /rate - Актуальний курс валют
        /convert - Почати конвертацію
        Вихідна валюта — це валюта, з якої ви хочете зробити обмін
        Цільова валюта — це валюта, в яку ви хочете конвертувати гроші
        Ви можете ввести 'Exit' на будь якому кроці конвертації, щоб скасувати її
    """
    bot.send_message(chat_id, help_message)


@bot.message_handler(commands=['rate'])
def handler_rate(message):
    rate = f"""
                        Поточний курс основних валют
    UAH(₴) -> USD($) = {round(data[0]['rateBuy'], 2)} (купівля) / {round(data[0]['rateSell'], 2)} (продаж)
    UAH(₴) -> EUR(€) = {round(data[1]['rateBuy'], 2)} (купівля) / {round(data[1]['rateSell'], 2)} (продаж)
    EUR(€) -> USD($) = {round(data[2]['rateBuy'], 2)} (купівля) / {round(data[2]['rateSell'], 2)} (продаж)
    """
    bot.send_message(message.chat.id, rate)


@bot.message_handler(commands=['convert'])
def handler_convert(message):
    user_data.clear()
    bot.send_message(message.chat.id, 'Введіть суму для конвертації. Приклад: 500')
    if message.text.strip().lower() == 'exit':
        bot.send_message(message.chat.id, 'Операцію завершено')
        return
    bot.register_next_step_handler(message, convert_get_sum)


def convert_get_sum(message):
    if message.text.strip().lower() == 'exit':
        bot.send_message(message.chat.id, 'Операцію завершено')
        return
    try:
        sum_ = float(message.text)
        user_data['source_currency_sum'] = sum_
        bot.send_message(message.chat.id, 'Введіть вихідну валюту для конвертації. Приклад: UAH')
        bot.register_next_step_handler(message, convert_get_source_currency)

    except ValueError:
        bot.send_message(message.chat.id, 'Сталася помилка. Введіть коректну суму.')
        bot.register_next_step_handler(message, convert_get_sum)


def convert_get_source_currency(message):
    user_data['source_currency'] = message.text.upper()
    msg = message.text.upper()
    markup = types.InlineKeyboardMarkup()
    if message.text.strip().lower() == 'exit':
        bot.send_message(message.chat.id, 'Операцію завершено')
        return
    if msg in ['UAH', 'ГРИВНЯ', 'ГРН']:
        btn1 = types.InlineKeyboardButton(text="USD", callback_data="usd_from_uah")
        btn2 = types.InlineKeyboardButton(text="EUR", callback_data="eur_from_uah")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, 'Виберіть цільову валюту', reply_markup=markup)
    elif msg in ['USD', 'ДОЛАР']:
        btn1 = types.InlineKeyboardButton(text="UAH", callback_data="uah_from_usd")
        btn2 = types.InlineKeyboardButton(text="EUR", callback_data="eur_from_usd")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, 'Виберіть цільову валюту', reply_markup=markup)
    elif msg in ['EUR', 'ЄВРО']:
        btn1 = types.InlineKeyboardButton(text="UAH", callback_data="uah_from_eur")
        btn2 = types.InlineKeyboardButton(text="USD", callback_data="usd_from_eur")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, 'Виберіть цільову валюту', reply_markup=markup)
    elif msg not in ['EUR', 'ЄВРО', 'UAH', 'ГРИВНЯ', 'ГРН', 'USD', 'ДОЛАР']:
        bot.send_message(message.chat.id, 'Сталася помилка. Введіть коректну валюту.')
        bot.register_next_step_handler(message, convert_get_source_currency)


@bot.callback_query_handler(func=lambda call: call.data == "usd_from_uah")
def handle_usd_from_uah_callback(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Вибрано долари')
    result = round(user_data['source_currency_sum'] / data[0]['rateBuy'], 2)
    save_conversation_request({
        'user_id': call.from_user.id,
        'source_currency': user_data['source_currency'],
        'target_currency': 'USD',
        'sum': user_data['source_currency_sum'],
        'result': result
    })
    bot.send_message(call.message.chat.id,
                     f"Ваші {user_data['source_currency_sum']} UAH(₴) можна конвертувати у {result} USD($)")


@bot.callback_query_handler(func=lambda call: call.data == "eur_from_uah")
def handle_eur_from_uah_callback(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Вибрано євро')
    result = round(user_data['source_currency_sum'] / data[1]['rateBuy'], 2)
    save_conversation_request({
        'user_id': call.from_user.id,
        'source_currency': user_data['source_currency'],
        'target_currency': 'EUR',
        'sum': user_data['source_currency_sum'],
        'result': result
    })
    bot.send_message(call.message.chat.id,
                     f"Ваші {user_data['source_currency_sum']} UAH(₴) можна конвертувати у {result} EUR(€)")


@bot.callback_query_handler(func=lambda call: call.data == "uah_from_usd")
def handle_uah_from_usd_callback(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Вибрано гривні')
    result = round(user_data['source_currency_sum'] * data[0]['rateSell'], 2)
    save_conversation_request({
        'user_id': call.from_user.id,
        'source_currency': user_data['source_currency'],
        'target_currency': 'UAH',
        'sum': user_data['source_currency_sum'],
        'result': result
    })
    bot.send_message(call.message.chat.id,
                     f"Ваші {user_data['source_currency_sum']} USD($) можна конвертувати у {result} UAH(₴)")


@bot.callback_query_handler(func=lambda call: call.data == "eur_from_usd")
def handle_eur_from_usd_callback(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Вибрано євро')
    result = round(user_data['source_currency_sum'] / data[2]['rateSell'], 2)
    save_conversation_request({
        'user_id': call.from_user.id,
        'source_currency': user_data['source_currency'],
        'target_currency': 'EUR',
        'sum': user_data['source_currency_sum'],
        'result': result
    })
    bot.send_message(call.message.chat.id,
                     f"Ваші {user_data['source_currency_sum']} USD($) можна конвертувати у {result} EUR(€)")


@bot.callback_query_handler(func=lambda call: call.data == "uah_from_eur")
def handle_uah_from_eur_callback(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Вибрано гривні')
    result = round(user_data['source_currency_sum'] * data[1]['rateSell'], 2)
    save_conversation_request({
        'user_id': call.from_user.id,
        'source_currency': user_data['source_currency'],
        'target_currency': 'UAH',
        'sum': user_data['source_currency_sum'],
        'result': result
    })
    bot.send_message(call.message.chat.id,
                     f"Ваші {user_data['source_currency_sum']} EUR(€) можна конвертувати у {result} UAH(₴)")


@bot.callback_query_handler(func=lambda call: call.data == "usd_from_eur")
def handle_eur_from_usd_callback(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Вибрано долари')
    result = round(user_data['source_currency_sum'] * data[2]['rateSell'], 2)
    save_conversation_request({
        'user_id': call.from_user.id,
        'source_currency': user_data['source_currency'],
        'target_currency': 'USD',
        'sum': user_data['source_currency_sum'],
        'result': result
    })
    bot.send_message(call.message.chat.id,
                     f"Ваші {user_data['source_currency_sum']} EUR(€) можна конвертувати у {result} USD($)")


bot.polling()
