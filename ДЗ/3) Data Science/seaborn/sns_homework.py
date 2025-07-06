import seaborn as sns
from matplotlib import pyplot as plt

penguins = sns.load_dataset('penguins')

print(penguins.head())
print(penguins.columns)

sns.scatterplot(data=penguins, x='bill_length_mm', y='body_mass_g') # Розподіл ваги та висоти птахів
plt.show()


sns.boxplot(data=penguins, x='species', y='flipper_length_mm', hue='species') # Розміри крил в залежності від виду птаха
plt.show()


plt.figure(figsize=(12, 6))
corr = penguins.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True , cmap='coolwarm') # Кореляція між різними ознаками пінгвінів
plt.show()
# Найбільш залежними є довжина крил (flipper_length_mm) та маса тіла (body_mass_g).
# Також прослідковується якась залежність довжиною крил (flipper_length_mm) та довжиною тіла пінгвінів (bill_length_mm)