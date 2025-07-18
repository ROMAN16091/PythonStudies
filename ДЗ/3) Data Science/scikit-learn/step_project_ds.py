import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Завантажуємо набір даних
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)
print(df.head())

# Обробляємо відсутні значення
print(df.isna().sum(),'\n')
df['Age'] = df['Age'].fillna(df['Age'].mean()) # Заповняємо відсутній вік середнім
df['Deck'] = df['Cabin'].str[0] # Створюємо колонку Deck, яка вказує на палубу пасажира
df['Deck'] = df['Deck'].fillna(df['Deck'].mode()[0]) # Заповняємо відсутню палубу модою
df = df.drop(columns='Cabin') # Видаляємо колонку з каютою
print(df.isna().sum())

# Кодуємо категоріальні змінні
df = pd.get_dummies(df, columns=['Embarked']) # Кодуємо порт з якого пасажир сів на корабель
df = pd.get_dummies(df, columns=['Sex']) # Кодуємо стать людей
print(df.head())

# Видаляємо характеристики, які можуть не вносити вкладу в модель
df = df.drop(columns='Ticket')

# Аналіз розподілу ключових характеристик та їх зв'язку з цільовою змінною Survived






# Інженерія ознак
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1 # Розмір сім‘ї
print(df['FamilySize'], '\n')

df['IsAlone'] = ((df['SibSp'] == 0) & (df['Parch'] == 0)) # Чи був пасажир один на кораблі
print(df['IsAlone'],'\n')

df['Title'] = df['Name'].str.split(', ').str[1].str.split('. ').str[0] # Робимо колонку з титулом
print(df['Title'])




