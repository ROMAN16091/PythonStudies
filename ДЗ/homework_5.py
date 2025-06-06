import sqlite3
from bs4 import BeautifulSoup
import requests


conn = sqlite3.connect('iphones_info.db')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS phones_info
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
model TEXT,
price TEXT,
disc_price TEXT,
reviews_count TEXT,
model_link TEXT,
description TEXT)
""")

url = 'https://rozetka.com.ua/ua/mobile-phones/c80003/producer=apple/'
cont = requests.get(url).text
soup = BeautifulSoup(cont, 'lxml')
models = soup.find_all('a', class_='tile-image-host')
prices = soup.find_all('div', class_ = 'old-price mb-1')
disc_prices = soup.find_all('div', class_ = 'price color-red')
reviews_counts = soup.find_all('span', class_ = 'rating-block-content')
links = [l.get('href') for l in soup.find_all('a', class_='tile-image-host')]

for model, price, disc_price, review, link in zip(models , prices, disc_prices, reviews_counts, links):
    page = requests.get(link)
    soup2 = BeautifulSoup(page.text, 'lxml')
    desc_block = soup2.find('p', class_='mt-4')
    description = desc_block.text.strip()
    price = price.text.replace('\xa0', ' ').strip()
    disc_price = disc_price.text.replace('\xa0', ' ').strip()
    cur.execute('INSERT INTO phones_info (model, price, disc_price, reviews_count, model_link, description) VALUES (?, ?, ?, ?, ?, ?)',
                (model.get('title'), price, disc_price, review.text.strip(), link, description))
print('Виконано!')
conn.commit()
conn.close()