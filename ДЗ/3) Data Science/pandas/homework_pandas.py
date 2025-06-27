import pandas as pd

columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
iris_df = pd.read_csv('iris.csv', header=None, names=columns)

print(iris_df.groupby('class')['sepal_length'].mean().reset_index()) # Cередня довжина чашелистика для кожного виду ірису
print()

iris_setosa = iris_df[iris_df['class'] == 'Iris-setosa']
max_petal_width_setosa = iris_setosa.groupby('class')['petal_width'].max().reset_index(drop=True).iloc[0]
print(f'Max petal width for iris setosa: {max_petal_width_setosa}') # Максимальна ширина листка для виду "setosa"
print()

print(iris_df['petal_length'].describe()) # Розподіленість довжини листка для всіх ірисів
print()
print()


iris_versicolor_df = iris_df[iris_df["class"] == 'Iris-versicolor'].reset_index(drop=True)

print(iris_df[iris_df['petal_length'] > 5.0].reset_index(drop=True)) # Фільтрація даних для ірисів з довжиною листка більше 5
print()


print(iris_df.groupby('class')['petal_width'].mean().reset_index()) # Середня ширина листка для кожного виду ірису
print()

print(iris_df.groupby('class')['sepal_length'].min().reset_index()) # Мінімальна довжина чашелистика для кожного виду ірису

print()

mean_petal_length = iris_df['petal_length'].mean()
high_petal_length_counts = iris_df[iris_df['petal_length'] > mean_petal_length].value_counts().reset_index() # Іриси, з довжиною листка вище середньої
print(high_petal_length_counts.groupby('class')['count'].sum().reset_index()) # Кількість ірисів з довжиною листка вище середньої
