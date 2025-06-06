import asyncio
import random
import time
import threading
import requests
import aiohttp
import multiprocessing
# async def download_file(name):
#     print(f'Start downloading file {name}')
#     await asyncio.sleep(1)
#     return 'Downloaded file {name}'
#
#
# async def main():
#     tasks = [
#         asyncio.create_task(download_file('file1')),
#         asyncio.create_task(download_file('file2')),
#         asyncio.create_task(download_file('file3')),
#     ]
#     await asyncio.gather(*tasks)
#
# result = asyncio.run(main())
# print(result)

# async def integral(name):
#     delay = random.randint(1, 5)
#     print(f'Delay for {name} -> {delay}')
#     await asyncio.sleep(delay)
#
#
# async def slow_task(name):
#     await integral(name)
#     return f'{name} finish'
#
# async def main():
#     tasks = [slow_task(f'Task {i}') for i in range(5)]
#
#     for finished in asyncio.as_completed(tasks):
#         result = await finished
#         print(result)
#
# asyncio.run(main())


# async def get_from_db(product_id):
#     print(f'Шукаємо товар {product_id} в БД...')
#     await asyncio.sleep(1.5)
#     return {'id': product_id, 'name': 'Ноутбук', 'stock': 7}
#
# async def get_external_price(product_id):
#     print(f'Отримаємо ціну з АРІ для {product_id}...')
#     await asyncio.sleep(1)
#     return round(random.uniform(500,700))
#
# async def handle_request(product_id):
#     print(f'Обробляємо запит для товару {product_id}...')
#     db_task = asyncio.create_task(get_from_db(product_id))
#     price_task = asyncio.create_task(get_external_price(product_id))
#     product_data = await db_task
#     price = await price_task
#     response = {
#         'product': product_data['name'],
#         'stock': product_data['stock'],
#         'price_usd': price
#     }
#     print(f'Відповідь для користувача: {response}')
#
# async def main():
#     product_ids = [101, 102, 103]
#     tasks = [handle_request(pid) for pid in product_ids]
#     await asyncio.gather(*tasks)
#
# start = time.time()
# print(start)
# asyncio.run(main())
# end = time.time()
# print(f'Total time: {end - start}')


# import asyncio
# import random
#
# async def check_user_login(username, password):
#     print(f'Перевіряємо користувача {username}')
#     await asyncio.sleep(1)
#     return username == 'admin' and password == '123'
#
# async def login_controller(username, password):
#     is_valid = await check_user_login(username, password)
#     if is_valid:
#         print('OK')
#     else:
#         print('NO')
#
# async def receive_msg(user):
#     await asyncio.sleep(random.uniform(0.5, 2))
#     print(f'{user} send msg')
#
# async def chat_simulation():
#     users = ['Anna', 'Ivan', 'Bob']
#     await asyncio.gather(*(receive_msg(user) for user in users))
#
# async def main():
#     print('\n----Login----')
#     await login_controller('user', '1234')
#     await login_controller('admin', '123')
#
#     print('\n----Chat----')
#     await chat_simulation()
#
# asyncio.run(main())

# urls = [
#     "https://www.google.com",
#     "https://www.example.com",
#     "https://www.python.org",
# ]
#
#
# def fetch(url):
#     responses = requests.get(url)
#     print(f'[Threading]: {len(responses.content)} bytes')
#
#
# start = time.time()
# threads = []
#
# for url in urls:
#     thread = threading.Thread(target=fetch, args = (url,))
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# print(f'Total time: {time.time() - start:.2f} seconds')


# async def fetch(session, url):
#     async with session.get(url) as response:
#         content = await response.read()
#         print(f'[Asyncio] {url} {len(content)} bytes')
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         tasks = [fetch(session, url) for url in urls]
#         await asyncio.gather(*tasks)
#
# start = time.time()
# asyncio.run(main())
# print(f'Total time: {time.time() - start:.2f}')


