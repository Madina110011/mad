'''import seaborn as sns

# Загрузка набора данных "tips" из Seaborn
tips_df = sns.load_dataset('tips')

# Вывод первых нескольких строк DataFrame
print(tips_df.head())'''

'''import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка набора данных "tips" из Seaborn
tips_df = sns.load_dataset('tips')

# Создание графика с двумя гистограммами
sns.histplot(data=tips_df, x='total_bill', color='blue', label='Total Bill', kde=True)
sns.histplot(data=tips_df, x='tip', color='red', label='Tip', kde=True)

# Добавление подписей к осям и заголовка
plt.xlabel('Amount ($)')
plt.ylabel('Frequency')
plt.title('Histogram of Total Bill and Tips')

# Добавление легенды
plt.legend()

# Отображение графика
plt.show()'''


'''import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка набора данных "tips" из Seaborn
tips_df = sns.load_dataset('tips')

# Создание графика с двумя гистограммами
sns.histplot(data=tips_df, x='total_bill', color='blue', label='Total Bill', kde=True, alpha=0.7)
sns.histplot(data=tips_df, x='tip', color='red', label='Tip', kde=True, alpha=0.7)

# Настройка внешнего вида графика
plt.xlabel('Amount ($)')
plt.ylabel('Frequency')
plt.title('Histogram of Total Bill and Tips')

# Добавление легенды
plt.legend()

# Отображение графика
plt.show()''' 


'''import seaborn as sns

# Загрузка набора данных "flights" из Seaborn
flights_df = sns.load_dataset('flights')

# Просмотр первых нескольких строк DataFrame
print(flights_df.head())''' 

'''import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка набора данных "flights" из Seaborn
flights_df = sns.load_dataset('flights')

# Создание матрицы корреляции
correlation_matrix = flights_df.pivot_table(index='month', columns='year', values='passengers')

# Создание тепловой карты
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='g')

# Настройка внешнего вида графика
plt.title('Correlation Between Months and Passengers')
plt.xlabel('Year')
plt.ylabel('Month')

# Отображение графика
plt.show()''' 

'''import seaborn as sns

# Загрузка набора данных "diamonds" из seaborn-data
diamonds_df = sns.load_dataset('diamonds')

# Просмотр первых нескольких строк DataFrame
print(diamonds_df.head())''' 

import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка набора данных "diamonds" из seaborn-data
diamonds_df = sns.load_dataset('diamonds')

# Построение ящика с усами для переменной "price" с разделением по качеству ("cut")
plt.figure(figsize=(10, 6))
sns.boxplot(data=diamonds_df, x='cut', y='price', palette='coolwarm')

# Настройка внешнего вида графика
plt.title('Boxplot of Price by Cut Quality')
plt.xlabel('Cut Quality')
plt.ylabel('Price')

# Отображение графика
plt.show()