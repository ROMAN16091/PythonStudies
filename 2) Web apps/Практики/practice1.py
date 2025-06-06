# Опис функціоналу:
# Ініціалізація бази даних: Створити таблицю замовлень у базі даних SQLite, якщо вона ще не існує.
# Створення замовлення: Для кожного замовлення згенерувати випадкові дані: ID, email користувача, список товарів та суму замовлення.
# Обробка замовлення:
# Отримання замовлення: Додати замовлення в базу даних з початковим статусом "received".
# Імітація оплати: Після затримки змінити статус на "paid".
# Імітація збереження в базі: Після наступної затримки змінити статус на "saved_to_db".
# Імітація відправки email: Після ще однієї затримки змінити статус на "email_sent".
# Завершення обробки: Після всіх етапів змінити статус на "completed".
# Обробка замовлень воркерами: Створити кілька воркерів (асинхронних робітників), які будуть по черзі обробляти замовлення з черги.
# Черга замовлень: Замовлення додаються до черги для обробки воркерами, і кожен воркер забирає замовлення та обробляє його.
# Завершення процесу: Коли всі замовлення оброблені, система повинна коректно завершити роботу.
# Деталі:
# Використовуються асинхронні функції для обробки замовлень та збереження їх у базу даних.
# Для кожного етапу обробки замовлення є затримки, які імітують реальні процеси (наприклад, час на оплату, збереження та відправку email).
# Потрібно використати SQLite для зберігання замовлень та їх статусів.
# Завдання:
# Реалізувати систему для асинхронної обробки замовлень у базі даних SQLite.
# Додати функціонал для створення фейкових замовлень.
# Створити воркерів для обробки замовлень та зміни їх статусів.
# Підключити чергу замовлень і обробляти їх паралельно.




import asyncio
import random
import aiosqlite
import sqlite3
from typing import Dict
from datetime import datetime, timedelta

# DB_PATH = 'orders.db'
# def init_db():
#     with sqlite3.connect(DB_PATH) as db:
#         db.execute("""
#             CREATE TABLE IF NOT EXISTS orders (
#             id INTEGER PRIMARY KEY,
#             user_email TEXT,
#             items TEXT,
#             total REAL,
#             status TEXT
#             )
#         """)
#
#         db.commit()
#
# init_db()
#
# def create_oder(order_id: int) -> Dict:
#     return {
#         'id': order_id,
#         'user_email': f'user{order_id}@example.com',
#         'items': 'item1, item2',
#         'total': round(random.uniform(10, 100), 2)
#     }
#
# async def save_order_to_db(order: Dict, status: str):
#     async with aiosqlite.connect(DB_PATH) as db:
#         await db.execute("""
#             INSERT OR REPLACE INTO orders (id, user_email, items, total, status)
#             VALUES (?, ?, ?, ?, ?)
#         """, order['id'], order['user_email'], order['items'], order['total'], status)
#
# async def update_order_status(order_id: int, status: str):
#     async with aiosqlite.connect(DB_PATH) as db:
#         await db.execute("""
#             UPDATE orders SET status = ? WHERE id = ?
#         """),(status, order_id)
#         await db.commit()
#
# async def print_all_orders():
#     async with aiosqlite.connect(DB_PATH) as db:
#         async with db.execute("""SELECT * FROM orders""") as cursor:
#             rows = await cursor.fetchall()
#             for row in rows:
#                 print(row)
#
#             print()
#
# async def process_order(order: Dict):
#     print(f"Початок обробки #{order['id']}")
#     await save_order_to_db(order, "received")
#     await print_all_orders()
#
#     await asyncio.sleep(random.uniform(0.5, 1.5))
#     await update_order_status(order["id"], "paid")
#     print(f"Замовлення #{order['id']} оплачено")
#     await print_all_orders()
#
#     await asyncio.sleep(random.uniform(0.5, 1.5))
#     await update_order_status(order["id"], "email_sent")
#     print(f"Лист по амовленню #{order['id']} відправлено на {order['user_email']}")
#     await print_all_orders()
#
#     await asyncio.sleep(random.uniform(0.5, 1.5))
#     await update_order_status(order["id"], "email_sent")
#     print(f"Замовлення #{order['id']} завершено")
#     await print_all_orders()
#
# async def worker(worker_id: int, queue: asyncio.Queue):
#     while True:
#         order = await queue.get()
#         print(f'Воркер {worker_id} отримав замовлення #{order['id']}')
#         await process_order(order)
#         queue.task_done()
#
# async def main():
#     queue = asyncio.Queue()
#
#     workers = [asyncio.create_task(worker(i, queue)) for i in range(1,4)]
#
#     for i in range(1,11):
#         order = create_oder(i)
#         await queue.put(order)
#
#         print(f'Замовлення #{order['id']} додано до черги')
#
#     await queue.join()
#
#     for w in workers:
#         w.cancel()
#
#     await asyncio.gather(*workers, return_exceptions= True)
#
# asyncio.run(main())




# Задача: Система моніторингу температури з використанням асинхронного програмування
#
# Створіть асинхронну систему моніторингу температури сенсорів. Програма повинна:
#
# Ініціалізувати базу даних SQLite, створюючи таблицю temperatures, якщо вона ще не існує.
#
# Генерувати фейкові дані для 5 сенсорів кожні 2 секунди. Температура повинна бути випадковим числом у діапазоні від 20 до 80 °C.
#
# Зберігати ці дані в базу у таблицю temperatures, включаючи ідентифікатор сенсора, температуру та мітку часу.
#
# Опрацьовувати дані з черги асинхронними воркерами, які фіксують дані у базі та виводять повідомлення, якщо температура перевищує 60 °C.
#
# Перевіряти кожні 5 секунд середню температуру по кожному сенсору за останні 30 секунд. Якщо середнє значення перевищує 65 °C — виводити тривожне повідомлення.
#
# Забезпечити можливість перевірки кожної окремої функції вручну, для цього кожну функцію треба зробити такою, щоб її можна було запустити окремо для тестування.




DB_PATH = 'sensor.db'

def init_db():
    with sqlite3.connect(DB_PATH) as db:
        db.execute("""
        CREATE TABLE IF NOT EXISTS temperature (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sensor_id TEXT,
        temperature REAL,
        timestamp TEXT
        )
        """)

    db.commit()

init_db()

def get_sensor_data(sensor_id: int) -> Dict:
    return {
        'sensor_id': f'sensor_{sensor_id}',
        'temperature': round(random.uniform(20,80), 2),
        'timestamp': datetime.now()
    }

print(get_sensor_data(2))

async def save_temperature(data: Dict):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT INTO temperature (sensor_id, temperature, timestamp)
            VALUES (?, ?, ?)
        """, (data['sensor_id'], data['temperature'], data['timestamp']))

        await db.commit()

# async def t_save_temp():
#     data = get_sensor_data(2)
#     await save_temperature(data)
#
# asyncio.run(t_save_temp())

async def sensor_worker(worker_id: int, queue: asyncio.Queue):
    while True:
        data = await queue.get()
        print(f'Worker {worker_id} -> {data}')
        await save_temperature(data)
        if data['temperature'] > 60:
            print(f'ALARM {data['sensor_id']} high temperature ({data['temperature']})')
        queue.task_done()

async def sensor_scheduler(queue: asyncio.Queue):
    sensor_ids = [1,2,3,4,5]
    while True:
        await asyncio.sleep(2)
        for sensor_id in sensor_ids:
            data = get_sensor_data(sensor_id)
            await queue.put(data)
            print(f'Get new data from {data['sensor_id']}: {data['temperature']}')

    queue = asyncio.Queue()
    asyncio.run(sensor_scheduler(queue))

async def check_avg_temperature():
    while True:
        await asyncio.sleep(5)
        time_thrshold = datetime.now() - timedelta(seconds=30)
        async with aiosqlite.connect(DB_PATH) as db:
            async with db.execute("""
            SELECT sensor_id, temperature, timestamp FROM temperature
            """) as cursor:
                rows = await cursor.fetchall()
                if not rows:
                    print('No Data')
                    continue

                recent_data = [
                    (sensor_id, temp, timestamp)
                    for sensor_id, temp, timestamp in rows
                    if datetime.fromisoformat(timestamp) > time_thrshold
                ]


                if not recent_data:
                    print('No NEW DATA')
                    continue

                sensor_groups: Dict[str, list] = {}

                for sensor_id, temp, _ in recent_data:
                    sensor_groups.setdefault(sensor_id, []).append(temp)

                print('AVG temperature')
                for sensor_id, temps in sensor_groups.items():
                    avg_temp = sum(temps)/len(temps)
                    print(f'{sensor_id}: {avg_temp}:.2f')
                    if avg_temp > 65:
                        print(f'ALARM {sensor_id} avg temperature > 65')

init_db()
async def main():
    queue = asyncio.Queue
    workers = [asyncio.create_task(sensor_worker(i, queue)) for i in range(1,4)]
    producer = asyncio.create_task(sensor_scheduler(queue))
    avg_temp_checker = asyncio.create_task(check_avg_temperature())

    try:
        await asyncio.gather(producer, *workers, avg_temp_checker)
    except asyncio.CancelledError:
        print('EXIT')

asyncio.run(main())