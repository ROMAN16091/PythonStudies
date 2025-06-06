import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Product': ['A', 'B', 'C'],
    'Price': [10.5, 20.0, 25.25],
    'Quantity': [100, 50, 75]
}
df = pd.DataFrame(data)
print(df)

sns.histplot(df['Quantity'])
plt.show()