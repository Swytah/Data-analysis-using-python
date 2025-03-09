import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('sales_data.csv')

print(sales.head())
print(sales.shape)#rows and column
print(sales.info())#info 
print(sales.describe())# stats info

## Numerical analysis and visualization

print(sales['Unit_Cost'].describe())
print(sales['Unit_Cost'].mean())
print(sales['Unit_Cost'].median())

sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(14,6))
plt.show()

ax = sales['Unit_Cost'].plot(kind='density', figsize=(14,6))
ax.axvline(sales['Unit_Cost'].mean(), color='red')
ax.axvline(sales['Unit_Cost'].median(), color='green')
plt.show()

ax = sales['Unit_Cost'].plot(kind='hist', figsize=(14,6))
ax.set_ylabel('Number of Sales')
ax.set_xlabel('dollars')
plt.show()

## Categorical analysis and visualization

print(sales.head())
print(sales['Age_Group'].value_counts())

sales['Age_Group'].value_counts().plot(kind='pie', figsize=(6,6))
plt.show()

ax = sales['Age_Group'].value_counts().plot(kind='bar', figsize=(14,6))
ax.set_ylabel('Number of Sales')
plt.show()

## Relationship between the columns?

numeric_sales = sales.select_dtypes(include=['number'])
corr = numeric_sales.corr()
print(corr)

fig = plt.figure(figsize=(8,8))
plt.matshow(corr, cmap='RdBu', fignum=fig.number)
plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical')
plt.yticks(range(len(corr.columns)), corr.columns)
plt.show()

sales.plot(kind='scatter', x='Customer_Age', y='Revenue', figsize=(6,6))
plt.show()

sales.plot(kind='scatter', x='Revenue', y='Profit', figsize=(6,6))
plt.show()

ax = sales[['Profit', 'Age_Group']].boxplot(by='Age_Group', figsize=(10,6))
ax.set_ylabel('Profit')
plt.show()

boxplot_cols = ['Year', 'Customer_Age', 'Order_Quantity', 'Unit_Cost', 'Unit_Price', 'Profit']
sales[boxplot_cols].plot(kind='box', subplots=True, layout=(2,3), figsize=(14,8))
plt.show()

## Column wrangling

sales['Revenue_per_Age'] = sales['Revenue'] / sales['Customer_Age']
print(sales['Revenue_per_Age'].head())

sales['Revenue_per_Age'].plot(kind='density', figsize=(14,6))
plt.show()

sales['Revenue_per_Age'].plot(kind='hist', figsize=(14,6))
plt.show()

sales['Calculated_Cost'] = sales['Order_Quantity'] * sales['Unit_Cost']
print(sales['Calculated_Cost'].head())
print((sales['Calculated_Cost'] != sales['Cost']).sum())

sales.plot(kind='scatter', x='Calculated_Cost', y='Profit', figsize=(6,6))
plt.show()

sales['Calculated_Revenue'] = sales['Cost'] + sales['Profit']
print(sales['Calculated_Revenue'].head())
print((sales['Calculated_Revenue'] != sales['Revenue']).sum())
print(sales.head())

sales['Revenue'].plot(kind='hist', bins=100, figsize=(14,6))
plt.show()

print(sales['Unit_Price'].head())
sales['Unit_Price'] *= 1.03
print(sales['Unit_Price'].head())

## Selection & Indexing

print(sales.loc[sales['State'] == 'Kentucky'])
print(sales.loc[sales['Age_Group'] == 'Adults (35-64)', 'Revenue'].mean())
print(sales.loc[(sales['Age_Group'] == 'Youth (<25)') | (sales['Age_Group'] == 'Adults (35-64)')].shape[0])
print(sales.loc[(sales['Age_Group'] == 'Adults (35-64)') & (sales['Country'] == 'United States'), 'Revenue'].mean())
print(sales.loc[sales['Country'] == 'France', 'Revenue'].head())

sales.loc[sales['Country'] == 'France', 'Revenue'] *= 1.1
print(sales.loc[sales['Country'] == 'France', 'Revenue'].head())
