import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, recall_score, precision_score, confusion_matrix, ConfusionMatrixDisplay

penguins = sns.load_dataset('penguins') # Завантаження даних про пінгвінів

penguins = penguins.dropna() # Видалення записів з відсутніми значеннями

# Кодування категоріальних змінних (вид, острів, стать) за допомогою get_dummies
penguins = pd.get_dummies(penguins, columns=['island', 'sex'])
print(penguins)

# Розподіл даних на тренуючи та тестові в співвідношенні 80/20 (відповідно)
X = penguins.drop(columns=['species'])
y = penguins['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42 )

# Створення конвеєру для передобробки
model = RandomForestClassifier()
pipeline = Pipeline([
    ('scaler', StandardScaler()), # Масштабування
    ('classifier', model), # Класифікація
])
# Звертаємося до моделі у конвєері та передаємо гіперпараметри
param_grid = {'classifier__n_estimators': [50, 100, 150], 'classifier__max_depth': [5,10,15]}
grid_search = GridSearchCV(pipeline, param_grid, cv=5) # Створюємо модель пошуку
grid_search.fit(X_train, y_train)
print("Найкращі параметри:", grid_search.best_params_)

best_model = grid_search.best_estimator_ # Робимо удосконалену модель

# Тренуємо та робимо предікт
y_pred = best_model.predict(X_test)

# Оцінка точності, recall, precision F1-score
scores = cross_val_score(best_model, X_train, y_train, cv=5)
print(f'Результати: {scores.mean() * 100:.2f}%') # Результати крос - валідації для тренуючих даних
print(f'Точність: {best_model.score(X_test, y_test) * 100:.2f}%') # Точність моделі на тестових даних
print(f'Recall Score: {recall_score(y_test, y_pred, average='weighted')* 100:.2f}%') # Recall Score
print(f'Precision Score: {precision_score(y_test, y_pred, average='weighted')* 100:.2f}%') # Precision Score
print(f'F1 - score: {f1_score(y_test, y_pred, average='weighted')* 100:.2f}%') # F1 - Score

# Візуально відображаємо матрицю помилок
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=best_model.classes_)
disp.plot(cmap='Blues')
plt.title('Confusion Matrix')
plt.show()
