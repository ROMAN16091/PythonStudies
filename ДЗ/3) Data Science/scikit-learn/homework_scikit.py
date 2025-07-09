from sklearn.datasets import load_iris
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Завантаження даних
iris_data = load_iris()

# Перетворення Bunch об‘єкту у DataFrame
iris_df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
iris_df['target'] = iris_data.target # Додаємо колонку з числовим позначенням класу
iris_df['species'] = iris_df['target'].apply(lambda x: iris_data.target_names[x]) # Додаємо колонку з позначенням класу

# # Виводимо форму даних, тип даних та перші 3 рядки
# print(f'Форма даних: {iris_df.shape}\n')
# print(f'Тип даних:\n{iris_df.dtypes}\n')
# print(f'Перші 3 рядки: \n{iris_df.head(3)}\n')
#
# # Виводимо ключі, кількість рядків-стовпців, назви ознак та опис даних Ірису
# print(f'Ключі: {iris_df.keys()}\n')
# print(f'Кількість рядків-стовпців: {iris_df.columns}\n')
# print(f'Назви ознак: {iris_data.feature_names}\n')
# print(f'Опис даних Ірису:\n{iris_data.DESCR}\n')
#
# numeric_data = iris_df.select_dtypes(include='number') # Створюємо змінну де будуть тільки числові дані
#
# # Виводимо мінімальне та максимальне значення, перцентиль, середнє, стандартне відхилення
# print(f'Мінімальне: \n{numeric_data.min()}\n')
# print(f'Перцентиль %25 (Q1): \n{np.percentile(numeric_data, 25, axis=0)}\n')
# print(f'Перцентиль %50 (Q2, Медіана): \n{np.percentile(numeric_data, 50, axis=0)}\n')
# print(f'Перцентиль %75 (Q3): \n{np.percentile(numeric_data, 75, axis=0)}\n')
# print(f'Максимальне: \n{numeric_data.max()}\n')
# print(f'Середнє: \n{numeric_data.mean()}\n')
# print(f'Стандартне відхилення: \n{numeric_data.std()}\n')
#
#
# # Робимо спостереження для кожого виду
#
# print(f'Setosa: \n{iris_df[iris_df['species'] == 'setosa']}\n')
# print(f'Versicolor: \n{iris_df[iris_df['species'] == 'versicolor']}\n')
# print(f'Virginica: \n{iris_df[iris_df['species'] == 'virginica']}\n')
#
#
# # Cтворюємо графік для отримання загальної статистики даних Ірис та стовпчасту діаграму для визначення частоти трьох видів Ірис.
#
# cols = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'species']
# g = sns.pairplot(iris_df[cols], hue='species', height=1.5)
# g.fig.suptitle('General Statistics', y=1.0001)
# plt.show()
#
# sns.countplot(x='species', data=iris_df, hue='species')
# plt.title('Частота трьох видів Ірису')
# plt.xlabel('Вид ірису')
# plt.ylabel('Частота зустрічання')
# plt.show()

# Розподіл набору даних ірисів на його атрибути (X) та мітки (y)

X = iris_df.iloc[:, :4]
y = iris_df['species']
print(X.head())
print(y.head())

# Розділення набору даних ірисів на 70% тренувальних даних та 30% тестових даних
X_train_1, X_test_1, y_train_1, y_test_1 = train_test_split(X, y, test_size=0.3, random_state=42)

# Вивід цих наборів
print(f'Тренувальний набір даних:\n{X_train_1}\n'
      f'Тестовий набір даних:\n{X_test_1}\n')

# Стовпець з числовим позначенням класу вже існує
print(iris_df['target'])

# Розділення набору даних ірисів на 80% тренувальних даних та 20% тестових даних

X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X, y, test_size=0.2, random_state=42)

print(f'Тренувальний набір даних:\n{X_train_2}\n'
      f'Тестовий набір даних:\n{X_test_2}\n')

# Розділення набору даних ірисів на 70% тренувальних даних та 30% тестових даних
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = KNeighborsClassifier(n_neighbors=5) # Використовуємо K Nearest Neighbor Classifier для класифікації
# Тренуємо та робимо predict
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f'Точність: {(accuracy_score(y_test, y_pred)) * 100}%') # Виводимо точність передбачання
