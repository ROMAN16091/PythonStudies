import pandas as pd
#
data = {
    'Product': ['A', 'B', 'C'],
    'Price': [10.5, 20.0, 25.25],
    'Quantity': [100, 50, 75]
}

df = pd.DataFrame(data)
print(df)
#
# df.index  = ['row1', 'row2', 'row3']
#
# print(df)
# print('\n')
# print(df['Product']['row1'])
#
# df.columns = ['ProductName', 'UnitPrice', 'Stock']
# print(df)
#
# df.to_csv('data.csv')

df.columns = ["ProductName", "UnitPrice", "Stock"]
print(df)
df.to_csv("data.csv")
data = pd.read_csv('data.csv')
print(data)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import seaborn as sns

df = sns.load_dataset("iris")
# print(df)
X = df.drop(labels='species', axis=1)
y = df['species']
# print(X)
# print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# print(X_train)
print(X_test)
print(y_test)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
