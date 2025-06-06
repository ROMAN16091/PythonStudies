# База даних
# Файл бази даних: heroes.db.
# Таблиці:
# heroes
# id (INTEGER, PRIMARY KEY AUTOINCREMENT)
# name (TEXT) — ім’я героя
# hp (INTEGER) — початкові очки життя
# attack (INTEGER) — базова атака
#
# battle_log
# id (INTEGER, PRIMARY KEY AUTOINCREMENT)
# attacker (TEXT) — ім’я атакуючого
# defender (TEXT) — ім’я того, кого атакували
# damage (INTEGER) — заподіяний урон
#
# hero_modifiers
# hero_id (INTEGER) — ID героя
# bonus_against_id (INTEGER) — ID героя, проти якого є бонус
# weak_against_id (INTEGER) — ID героя, проти якого герой слабкий
#
# Початкове заповнення
# Функції seed_heroes() та seed_modifiers() додають до бази стандартний
# набір героїв та їхніх взаємних модифікаторів.
#
# Вибір команд
# Вивести список усіх героїв із їхніми параметрами.
# Користувач обирає 5 героїв для Команди 1 за допомогою їхніх ID.
# Інші 5 випадково формують Команду 2.
#
# Асинхронний бій
# Кожен герой запускає корутину fight(), яка:
# Пауза 1–2 секунди між атаками (asyncio.sleep).
# Вибір випадкового живого ворога з протилежної команди.
# Обчислення випадкового урону від 1 до attack.
# Застосування бонусів/слабкостей із таблиці hero_modifiers (множник ×1.5).
# Зменшення HP ворога, логування події в таблицю battle_log (за допомогою aiosqlite).
# Повідомлення про смерть героя, якщо hp ≤ 0.
# Якщо всі вороги мертві, корутина завершується з оголошенням переможця.
#
# Підсумок бою
# Після завершення всіх корутин збирається статистика загального урону,
# завданого кожним героєм (з таблиці battle_log).
# Виводиться рейтинг героїв за сумарним уроном.
# Очищення журналу бою для наступного запуску.

import asyncio
import random
import sqlite3
from dataclasses import dataclass
import aiosqlite

DB_NAME = 'heroes.db'

def create_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS heroes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    hp INTEGER,
    attack INTEGER
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS battle_log(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    attacker TEXT,
    defender TEXT,
    damage INTEGER
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS hero_modifiers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hero_id INTEGER,
        bonus_against_id INTEGER,
        weak_against_id INTEGER
    )
    """)
    conn.commit()
    conn.close()

def seed_heroes():
    heroes = [
        ('Wizard', 100, 15),
        ('Rogue', 80, 20),
        ('Knight', 120, 10),
        ('Dragon', 150, 25),
        ('Elf', 90, 18),
        ('Necromancer', 95, 16),
        ('Fire Djinn', 110, 22),
        ('Ice Witch', 85, 19),
        ('Barbarian', 130, 14),
        ("Ghost", 70, 23),
        ("Assassin", 75, 24)
    ]

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.executemany('INSERT INTO heroes (name, hp, attack) VALUES (?, ?, ?)', heroes)
    conn.commit()
    conn.close()

def seed_modifiers():
    modifiers = [
        (1,4,5), (2,5,6), (3,6,7),
        (4,1,8), (5,2,9), (6,3,10),
        (7,9,1), (8,10,11), (9,11,3),
        (10,7,2), (11,8,4)
    ]

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.executemany('INSERT INTO hero_modifiers (hero_id, bonus_against_id, weak_against_id) VALUES (?, ?, ?)', modifiers)
    conn.commit()
    conn.close()

def fetch_all_heroes():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM heroes')
    data = c.fetchall()
    conn.close()
    return data

def fetch_all_hero_modifiers():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT hero_id, bonus_against_id, weak_against_id FROM hero_modifiers')
    data = c.fetchall()
    conn.close()

    bonus_map = {}
    weak_map = {}

    for hero_id, bonus_id, weak_id in data:
        if bonus_id:
            bonus_map.setdefault(hero_id, set()).add(bonus_id)
        if weak_id:
            weak_map.setdefault(hero_id, set()).add(weak_id)  # Фіксована помилка

    return bonus_map, weak_map

async def log_damage(attacker, defender, damage):
    async with aiosqlite.connect(DB_NAME) as conn:
        async with conn.cursor() as c:
            await c.execute('INSERT INTO battle_log (attacker, defender, damage) VALUES (?, ?, ?)', (attacker, defender, damage))
            await conn.commit()

def print_battle_summary():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        SELECT attacker, SUM(damage) FROM battle_log GROUP BY attacker ORDER BY SUM(damage) DESC
    """)

    results = c.fetchall()
    print('\nСтатистика урона: ')
    for attacker, total in results:
        print(f'{attacker}: {total}')

    c.execute('DELETE FROM battle_log')
    conn.commit()
    conn.close()

@dataclass
class Hero:
    id: int
    name: str
    hp: int
    attack: int
    team: str
    heroes: list
    lock: asyncio.Lock
    bonus_map: dict
    weak_map: dict

    def is_alive(self):
        return self.hp > 0

    async def fight(self):
        while True:
            await asyncio.sleep(random.uniform(1,2))

            if not self.is_alive():
                return

            async with self.lock:
                enemies = [h for h in self.heroes if h.team != self.team and h.is_alive()]

                if not enemies:
                    print(f'\n{self.name} ({self.team}) виграв бій')
                    return

                target = random.choice(enemies)
                damage = random.randint(1, self.attack)

                # Модифікатори
                if target.id in self.bonus_map.get(self.id, set()):
                    damage = int(damage * 1.5)
                if target.id in self.weak_map.get(self.id, set()):
                    damage = int(damage * 0.75)

                target.hp -= damage
                print(f'{self.name} -> {target.name} {damage} HP: {max(target.hp, 0)}')
                await log_damage(self.name, target.name, damage)

                if target.hp <= 0:
                    print(f'{self.name} знищив {target.name} ({target.team})!!!')

def choose_heroes():
    all_heroes = fetch_all_heroes()
    print('Всі герої:')
    for h in all_heroes:
        print(f'{h[0]}. {h[1]} (HP: {h[2]}, Атака: {h[3]})')

    chosen_ids = set()
    team1 = []
    team2 = []

    while len(chosen_ids) < 5:
        try:
            hero_id = int(input(f'\nОбери героя №{len(chosen_ids) + 1}: '))
            if hero_id in chosen_ids:
                print('Вже обрано.')
            elif not any(h[0] == hero_id for h in all_heroes):
                print('Невірний ID.')
            else:
                chosen_ids.add(hero_id)
        except ValueError:
            print('Введи число (ID)')

    random.shuffle(all_heroes)
    for h in all_heroes:
        id_, name, hp, attack = h
        if id_ in chosen_ids:
            team1.append(Hero(id_, name, hp, attack, team='Команда 1', heroes=[], lock=None, bonus_map={}, weak_map={}))
        elif len(team2) < 5:
            team2.append(Hero(id_, name, hp, attack, team='Команда 2', heroes=[], lock=None, bonus_map={}, weak_map={}))

    print('\nКоманда 1:')
    for h in team1:
        print(h.name)
    print('\nКоманда 2:')
    for h in team2:
        print(h.name)

    return team1, team2

async def start_battle(team1, team2, bonus_map, weak_map):
    all_heroes = team1 + team2
    lock = asyncio.Lock()
    for h in all_heroes:
        h.heroes = all_heroes
        h.lock = lock
        h.bonus_map = bonus_map
        h.weak_map = weak_map

    tasks = [asyncio.create_task(hero.fight()) for hero in all_heroes]
    await asyncio.gather(*tasks)

def main():
    create_db()
    if input('Додати героїв та модифікатори (y/n): ').lower().strip() == 'y':
        seed_heroes()
        seed_modifiers()
        print('Додані герої та модифікатори.')

    team1, team2 = choose_heroes()
    bonus_map, weak_map = fetch_all_hero_modifiers()
    asyncio.run(start_battle(team1, team2, bonus_map, weak_map))
    print_battle_summary()

if __name__ == '__main__':
    main()
