# 1. Імпортуємо необхідні бібліотеки
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

# 2. Завантаження та попередній перегляд даних
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)
print("Перші 5 рядків:\n", df.head(), '\n')

# 3. Очищення та попередня обробка
print("Пропущені значення:\n", df.isna().sum(), '\n')
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Deck'] = df['Cabin'].str[0]
df['Deck'] = df['Deck'].fillna(df['Deck'].mode()[0])
df = df.drop(columns='Cabin')

# Заповнення порту посадки найчастішим
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])


# 4. Інженерія ознак
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['IsAlone'] = ((df['SibSp'] == 0) & (df['Parch'] == 0)).astype(int)
df['Title'] = df['Name'].str.extract(', ([A-Za-z]+)\.')[0]
df['Title'] = LabelEncoder().fit_transform(df['Title'])
df = df.drop(columns=['Name', 'Ticket'])  # Більше не потрібні

# 5. Кодування категоріальних змінних
df = pd.get_dummies(df, columns=['Embarked', 'Sex', 'Deck'], drop_first=True)

# 6. Розвідувальний аналіз даних (EDA)
sns.countplot(data=df, x='Survived')
plt.title("Кількість тих, хто вижив / не вижив")
plt.show()

sns.boxplot(data=df, x='Survived', y='Age')
plt.title("Розподіл віку за виживанням")
plt.show()

# 7. Розділення на X і y
X = df.drop(columns='Survived')
y = df['Survived']

# Масштабування ознак
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Розбиття на навчальну і тестову вибірки
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

# 8. Побудова моделі (Random Forest)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 9. Оцінка моделі
y_pred = model.predict(X_test)
print("Класифікаційний звіт:\n", classification_report(y_test, y_pred))
ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred)).plot()
plt.title("Матриця помилок")
plt.show()

cv_score = cross_val_score(model, X_scaled, y, cv=5).mean()
print(f"Середня точність на крос-валідації: {cv_score:.4f}")

# 10. Підбір параметрів (GridSearchCV)
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [4, 6, 8]
}
grid_search = GridSearchCV(model, param_grid, cv=5)
grid_search.fit(X_scaled, y)

print("Найкращі параметри:", grid_search.best_params_)
print(f"Точність з найкращими параметрами: {grid_search.best_score_:.4f}")
