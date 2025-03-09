import pandas as pd
data=pd.read_csv('googleplaystore.csv')
print(data)
##display top 5 row of the data
print(data.head(5))
#display last 3 rows of the data
print(data.tail(3))
#find shape of our dataset(number of rows and number of columns)
print(data.shape)
print(data.shape[0])
print(data.shape[1])
print(len(data.columns))
print(len(data))
#get information about our dataset like total number rows, total number of columns,datatypes of each column and memory requirement
print(data.info())
#get overall statistics about the dataframe
print(data.describe(include='all'))
#total number of app titles contain astrology
print(len(data[data['App'].str.contains('Astrology',case=False)]))
#find average app rating
print(data['Rating'].mean())
#find total number of unique category
print(data['Category'].nunique())
#which category getting the highest average rating
print(data.groupby('Category')['Rating'].mean().sort_values(ascending=False))
#find total number of apps having 5 star rating
print(len(data[data['Rating']==5.0]))
#find average value of reviews
data['Reviews']=data['Reviews'].replace('3.0M',3.0)
data['Reviews']=data['Reviews'].astype('float')
print(data['Reviews'].mean())
#find total number of free and paid apps
print(data['Type'].value_counts())
#which app has maximum reviews
print(data[data['Reviews'].max()==data['Reviews']]['App'])
#display top 5 apps having highest reviews
# Display top 5 apps with highest reviews
print(data.nlargest(5, 'Reviews')[['App', 'Reviews']])
print(data.sort_values(by='Reviews', ascending=False).head(5)[['App', 'Reviews']])
index=data['Reviews'].sort_values(ascending=False).head().index
print(data.iloc[index]['App'])
#find average rating of free and paid apps
print(data.groupby('Type')['Rating'].mean())
#display top 5 apps having maximum installs
data['Installs_1'] = data['Installs'].str.replace('+', '', regex=False)
data['Installs_1'] = data['Installs_1'].str.replace(',', '', regex=False)
data['Installs_1'] = data['Installs_1'].str.replace('Free', '0', regex=False)
'''
Regex (Regular Expression) is a sequence of characters that defines a search pattern, commonly used for string manipulation, pattern matching, and data validation.'''
data['Installs_1']=data['Installs_1'].astype(int)
index=data['Installs_1'].sort_values(ascending=False).head().index
print(data.iloc[index]['App'])
