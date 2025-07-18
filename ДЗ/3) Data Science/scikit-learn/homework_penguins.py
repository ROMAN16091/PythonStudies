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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Створення конвеєру для передобробки
model = RandomForestClassifier(class_weight='balanced', random_state=42, max_depth=5)
pipeline = Pipeline([
    ('scaler', StandardScaler()), # Масштабування
    ('classifier', model), # Класифікація
])
# Звертаємося до моделі у конвєері та передаємо гіперпараметри
param_grid = {'classifier__n_estimators': [50, 100, 150],
              'classifier__max_depth': [5,10,15],
              'classifier__min_samples_split': [2, 5, 10],
              'classifier__min_samples_leaf': [1, 2, 5],
              'classifier__max_features': ['sqrt', 'log2', None],

              }
grid_search = GridSearchCV(pipeline, param_grid, cv=5) # Створюємо модель пошуку
grid_search.fit(X_train, y_train)
pipeline.fit(X_train, y_train)
print("Найкращі параметри:", grid_search.best_params_)

best_model = grid_search.best_estimator_ # Робимо удосконалену модель

# Тренуємо та робимо предікт
y_pred_1 = best_model.predict(X_test)
y_pred_2 = pipeline.predict(X_test)

# Оцінка точності, recall, precision F1-score
scores_1 = cross_val_score(best_model, X_train, y_train, cv=5)
print(f'Результати: {scores_1.mean() * 100:.2f}%') # Результати крос - валідації для тренуючих даних
print(f'Точність: {best_model.score(X_test, y_test) * 100:.2f}%') # Точність моделі на тестових даних
print(f'Recall Score: {recall_score(y_test, y_pred_1, average='weighted')* 100:.2f}%') # Recall Score
print(f'Precision Score: {precision_score(y_test, y_pred_1, average='weighted')* 100:.2f}%') # Precision Score
print(f'F1 - score: {f1_score(y_test, y_pred_1, average='weighted')* 100:.2f}%') # F1 - Score
# Порівнняня з початковою моделлю
print()
scores_2 = cross_val_score(pipeline, X_train, y_train, cv=5)
print(f'Результати: {scores_2.mean() * 100:.2f}%') # Результати крос - валідації для тренуючих даних
print(f'Точність: {pipeline.score(X_test, y_test) * 100:.2f}%') # Точність моделі на тестових даних

# Візуально відображаємо матрицю помилок
disp1 = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred_1), display_labels=best_model.classes_)
disp1.plot(cmap='Blues')
plt.title('Confusion Matrix')
plt.show()
# Для початкової моделі також
disp2 = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred_2), display_labels=pipeline.classes_)
disp2.plot(cmap='Greens')
plt.title('Confusion Matrix')
plt.show()

# ВИСНОВКИ
# Початкова модель показує результати на пів відсотка менше (99.25%), ніж краща модель (99.62%). З інших тестів у них по 100%.
# Можна спробувати покращити результати крос - валідації до 100%. Матриця помилок також вказує, що вони все розподілили правильно.
# Типові помилки можуть бути ігнорування пустих значень, переобучення, та незбалансованість класів. Щодо планів на подальше
# дослідження, то можна спробувати використати інші класифікатори і обробити незбалансовані дані.