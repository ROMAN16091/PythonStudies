import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

conn = sqlite3.connect('iphones_info.db')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS phones_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    info TEXT,
    detailed_info TEXT,
    price TEXT,
    disc_price TEXT,
    reviews_count TEXT,
    model_link TEXT
)
""")

driver = webdriver.Chrome()
driver.get('https://rozetka.com.ua/ua/mobile-phones/c80003/producer=apple/')

# Очікуємо, поки зʼявиться хоча б один товар з новою структурою
WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.item'))
)

time.sleep(2)

items = driver.find_elements(By.CSS_SELECTOR, 'div.item')

for item in items:
    try:
        model_name = item.find_element(By.CSS_SELECTOR, 'a.tile-title').text.strip()
    except:
        model_name = ''

    detailed_info = ''  # В HTML блоку нема, залишаємо порожнім

    try:
        old_price = item.find_element(By.CSS_SELECTOR, 'div.old-price').text.strip()
    except:
        old_price = ''

    try:
        disc_price = item.find_element(By.CSS_SELECTOR, 'div.price.color-red').text.strip()
    except:
        disc_price = ''

    try:
        reviews = item.find_element(By.CSS_SELECTOR, 'rz-tile-rating a span.rating-block-content').text.strip()
    except:
        reviews = ''

    try:
        model_link = item.find_element(By.CSS_SELECTOR, 'a.tile-title').get_attribute('href')
    except:
        model_link = ''

    cur.execute('''
        INSERT INTO phones_info (info, detailed_info, price, disc_price, reviews_count, model_link)
        VALUES (?, ?, ?, ?, ?, ?)''',
        (model_name, detailed_info, old_price, disc_price, reviews, model_link)
    )

conn.commit()
conn.close()
driver.quit()
print('Готово!')
