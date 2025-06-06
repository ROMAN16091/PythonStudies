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