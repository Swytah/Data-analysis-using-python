import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

import pandas as pd

# Load the dataset
file_path = 'Udemy_Courses.csv'  # Update with your actual file path
df = pd.read_csv(file_path)

# Display initial info about the dataset
print("Initial DataFrame Info:")
print(df.info())
print("\nSample Data:")
print(df.head())

# Identify numeric columns and ensure correct data types
df_numeric = df.apply(pd.to_numeric, errors='coerce')

# Drop completely empty columns (if any)
df_numeric = df_numeric.dropna(axis=1, how='all')

# Check if a grouping column exists and is valid
grouping_column = 'your_grouping_column'  # Replace with the actual column name

if grouping_column in df_numeric.columns:
    # Perform groupby operation and calculate the mean
    df_grouped = df_numeric.groupby(grouping_column).mean()
    
    # Display result
    print("\nGrouped Data:")
    print(df_grouped)

    # Save the cleaned and grouped data to a new CSV file
    output_file = "grouped_data.csv"
    df_grouped.to_csv(output_file)
    print(f"\nGrouped data saved to: {output_file}")
else:
    print(f"Error: Grouping column '{grouping_column}' not found in the dataset.")
    df_grouped = None  # Ensuring df_grouped is always defined



























data = pd.read_csv('Udemy_Courses.csv', parse_dates=['published_timestamp'])  # parse_dates: parse_dates parameter for read_csv which allows you to define the names of the columns you want to be treated as dates or datetimes:
print(data.dtypes)
# display top 10 rows of the dataset
print(data.head(10))
# check last 5 rows of the dataset
print(data.tail(5))
# find shape of our dataset (number of rows and columns)
print(data.shape)
print(data.shape[0])  # rows
print(data.shape[1])  # column
# getting info about dataset
print(data.info())
# check null values
print(data.isnull().sum())
sns.heatmap(data.isnull())
plt.show()
# check for duplicate and drop them
du = data.duplicated().any()
print(du)
data = data.drop_duplicates()
# find out number of courses per subject
print(data['subject'].value_counts())
sns.countplot(x=data['subject'])
plt.xlabel("Subject", fontsize=13)
plt.ylabel("Number of courses per subject", fontsize=13)
plt.xticks(rotation=65)
plt.show()
# For Which Levels, Udemy Courses Providing The Courses
print(data['level'].value_counts())
sns.countplot(x=data['level'])
plt.xlabel("Level", fontsize=13)
plt.ylabel("Number of courses per level", fontsize=13)
plt.xticks(rotation=65)
plt.show()
# Display The Count of Paid and Free Courses
print(data['is_paid'].value_counts())
sns.countplot(x=data['is_paid'])
plt.xlabel("Is_paid", fontsize=13)
plt.ylabel("Number of Free and Paid courses", fontsize=13)
plt.xticks(rotation=65)
plt.show()
# Which Course Has More Lectures (Free or Paid)?
print(data.groupby(['is_paid']).mean())
# Which Courses Have A Higher Number of Subscribers Free or Paid?
sns.barplot(x="is_paid", y="num_subscribers", data=data)
plt.show()
# Which Level Has The Highest Number of Subscribers?
sns.barplot(x="level", y="num_subscribers", data=data)
plt.xticks(rotation=65)
plt.show()
# Find Most Popular Course Title
print(data[data['num_subscribers'] == data['num_subscribers'].max()][['course_title', 'num_subscribers']])
# Display 10 Most Popular Courses As Per Number of Subscribers
top = data.sort_values(by="num_subscribers", ascending=False).head(10)
sns.barplot(x="num_subscribers", y="course_title", data=top)
plt.show()
# Find The Course Which Is Having The Highest Number of Reviews.
plt.figure(figsize=(10, 4))
sns.barplot(x="subject", y="num_reviews", data=top)
plt.show()
# Does Price Affect the Number of Reviews?
plt.figure(figsize=(15, 6))
sns.scatterplot(x="price", y="num_reviews", data=data)
plt.show()
# Find Total Number of Courses Related To Python
print(len(data[data['course_title'].str.contains('python', case=False)]))
# Display 10 Most Popular Python Courses As Per Number of Subscribers
python = data[data['course_title'].str.contains('python', case=False)].sort_values(by="num_subscribers", ascending=False).head(10)
sns.barplot(x="num_subscribers", y="course_title", data=python)
plt.show()
# In Which Year The Highest Number of Courses Were Posted?
data['Year'] = data['published_timestamp'].dt.year
print(data.head(1))
sns.countplot(x='Year', data=data)
plt.show()
# Display Category-Wise Count of Posted Subjects [Year Wise]
print(data.groupby('Year')['subject'].value_counts())
