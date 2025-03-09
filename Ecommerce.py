import pandas as pd
data=pd.read_csv('Ecommerce Purchases')
print(data)
##display top 10 rows of the dataset
print(data.head(10))
##display last 10 rows of the dataset
print(data.tail(10))
##check datatype of each column
print(data.dtypes)
##check null values in the dataset
print(data.isnull().sum())
##how many rows and columns are there in our dataset?
print(len(data.columns))
print(len(data))
print(data.info())
##highest and lowest purchase prices
print(data['Purchase Price'].max())
print(data['Purchase Price'].min())
##average purchase price
print(data['Purchase Price'].mean())
##how many people have French 'fr' as their language?
print(len(data[data['Language']=='fr']))
print(data[data['Language']=='fr'].count())
##job title contains engineer
print(len(data[data['Job'].str.contains('Engineer',case=False)]))#case is for case sensitive
##find email of the person with the following  IP address:132.207.160.22
print(data[data['IP Address']=='132.207.160.22']['Email'])
##how many people have mastercard as their credit card provider and made a purchase above 50
print(len(data[(data['CC Provider']=='Mastercard') & (data['Purchase Price']>50)]))
##find email of the person with the following credit card number:466482525897302
print(data[data['Credit Card']==466482525897302]['Email'])
##how many people purchase during the AM and how many people purchase during PM
print(data['AM or PM'].value_counts())
##how many people have a credit card that expires in 2020
def fun():
    count=0
    for date in data['CC Exp Date']:
        if date.split('/')[1]=='20':
            count=count+1
    print(count)
fun()
print(len(data[data['CC Exp Date'].apply(lambda x:x[3:]=='20')]))
##top 5 most popular email providers(e.g. gamil.com,yahoo.com,etc...)
list1=[]
for email in data['Email']:
    list1.append(email.split('@')[1])
data['temp']=list1
print(data['temp'].value_counts().head(5))
print(data['Email'].apply(lambda x:x.split('@')[1]).value_counts().head())
