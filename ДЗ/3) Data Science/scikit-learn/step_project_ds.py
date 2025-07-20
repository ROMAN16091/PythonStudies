import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

# Завантажуємо набір даних із raw-посилання
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)
print(df.head(), '\n')

# Перевірка пропущених значень
print("Пропущені значення:\n", df.isna().sum(), '\n')

# Обробка пропущених значень
df['Age'] = df['Age'].fillna(df['Age'].mean())  # Заповнюємо пропуски у віці середнім
df['Deck'] = df['Cabin'].str[0]  # Витягуємо палубу з першої літери каюти
df['Deck'] = df['Deck'].fillna(df['Deck'].mode()[0])  # Заповнюємо пропущені палуби найчастішою
df = df.drop(columns='Cabin')  # Видаляємо колонку каюти, вона вже не потрібна

# Ще раз перевіримо пропуски
print("Після обробки:\n", df.isna().sum(), '\n')

# Кодуємо категоріальні змінні
df = pd.get_dummies(df, columns=['Embarked'])  # Embarked → Embarked_C, Embarked_Q, Embarked_S
df = pd.get_dummies(df, columns=['Sex'])  # Sex → Sex_female, Sex_male
df = pd.get_dummies(df, columns=['Deck'])  # Deck → одна колонка на кожну палубу
print("Після кодування:\n", df.head(), '\n')

# Видаляємо неінформативні колонки
df = df.drop(columns=['Ticket'])  # Номер квитка не несе корисної інформації

# Інженерія ознак
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1  # Кількість людей, що подорожували разом
df['IsAlone'] = ((df['SibSp'] == 0) & (df['Parch'] == 0)).astype(int)  # 1, якщо був один, 0 — ні
df['Title'] = df['Name'].str.split(', ').str[1].str.split('. ').str[0]  # Витягуємо титул з імені
df = df.drop(columns=['Name'])  # Після витягання титулу ім’я вже не потрібне

# Об’єднуємо рідкісні титули в одну групу
df['Title'] = df['Title'].replace(['Mlle', 'Ms', 'Lady', 'Countess', 'Mme'], 'Rare')
df['Title'] = df['Title'].replace(['Dr', 'Rev', 'Col', 'Major', 'Capt', 'Sir', 'Don', 'Jonkheer', 'Dona'], 'Rare')

# Кодуємо колонку Title
df['Title'] = LabelEncoder().fit_transform(df['Title'])

# Обробка залишків пропусків (наприклад, Fare у 1 рядку)
df = df.dropna()

# Розділяємо змінні на ознаки (X) та ціль (y)
X = df.drop('Survived', axis=1)
y = df['Survived']

# Масштабуємо ознаки (щоб не було великих розбіжностей у значеннях)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Розбиваємо на train/test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Навчаємо модель
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Оцінка на тестових даних
y_pred = model.predict(X_test)

# Крос-валідація
cv_score = cross_val_score(model, X_scaled, y, cv=5).mean()
print(f"Середня точність (крос-валідація): {cv_score:.4f}")

# Матриця помилок
ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred)).plot()
plt.title("Матриця помилок")
plt.show()

# Звіт класифікації
print("Класифікаційний звіт:\n", classification_report(y_test, y_pred))

# Пошук найкращих параметрів (опційно)
param_grid = {'n_estimators': [100, 200], 'max_depth': [4, 6, 8]}
grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5)
grid_search.fit(X_scaled, y)
print("Найкращі параметри:", grid_search.best_params_)
