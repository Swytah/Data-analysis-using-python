import numpy as np
import pandas as pd

# Creating DataFrame
df = pd.DataFrame({
    'Sex': ['M', 'F', 'F', 'D', '?'],
    'Age': [29, 30, 24, 290, 25],
})

print(df)
print(df['Sex'].unique())  # Unique values in 'Sex' column
print(df['Sex'].value_counts())  # Frequency count of each value in 'Sex'

# Replacing values in 'Sex' column
print(df['Sex'].replace('D', 'F'))
print(df['Sex'].replace({'D': 'F', 'N': 'M'}))

# Replacing values in both 'Sex' and 'Age' columns
df = df.replace({
    'Sex': {'D': 'F', 'N': 'M'},
    'Age': {290: 29}
})

print(df)

# Finding rows where 'Age' > 100
print(df[df['Age'] > 100])

# Corrected age values for those > 100
df.loc[df['Age'] > 100, 'Age'] = df.loc[df['Age'] > 100, 'Age'] / 10

print(df)  # Now 'Age' column is corrected

# Series with duplicate values
ambassadors = pd.Series([
    'France',
    'United Kingdom',
    'United Kingdom',
    'Italy',
    'Germany',
    'Germany',
    'Germany',
], index=[
    'Gérard Araud',
    'Kim Darroch',
    'Peter Westmacott',
    'Armando Varricchio',
    'Peter Wittig',
    'Peter Ammon',
    'Klaus Scharioth '
])

print(ambassadors)
print(ambassadors.duplicated())  # Check duplicate values
print(ambassadors.duplicated(keep='last'))
print(ambassadors.duplicated(keep=False))

# Dropping duplicates
print(ambassadors.drop_duplicates())  # Keep first occurrence
print(ambassadors.drop_duplicates(keep='last'))  # Keep last occurrence
print(ambassadors.drop_duplicates(keep=False))  # Drop all duplicates

# Creating another DataFrame with duplicates
players = pd.DataFrame({
    'Name': [
        'Kobe Bryant',
        'LeBron James',
        'Kobe Bryant',
        'Carmelo Anthony',
        'Kobe Bryant',
    ],
    'Pos': ['SG', 'SF', 'SG', 'SF', 'SF']
})

print(players)
print(players.duplicated())  # Check duplicate rows
print(players.duplicated(subset=['Name']))  # Check duplicate names only
print(players.duplicated(subset=['Name'], keep='last'))

# Dropping duplicates
print(players.drop_duplicates())  # Drops identical rows
print(players.drop_duplicates(subset=['Name']))  # Keeps first occurrence
print(players.drop_duplicates(subset=['Name'], keep='last'))  # Keeps last occurrence

# Creating DataFrame with structured text
df = pd.DataFrame({
    'Data': [
        '1987_M_US _1',
        '1990?_M_UK_1',
        '1992_F_US_2',
        '1970?_M_   IT_1',
        '1985_F_I  T_2'
]})

print(df)

# Splitting column into multiple columns
print(df['Data'].str.split('_'))  # Splitting without expanding
df = df['Data'].str.split('_', expand=True)  # Splitting into new columns

# Assign column names to avoid errors
df.columns = ['Year', 'Sex', 'Country', 'Code']

print(df)

# Fixing values in 'Year' column
print(df['Year'].str.contains(r'\?'))  # Checking if '?' exists in 'Year'
print(df['Country'].str.contains('U'))  # Checking if 'U' exists in 'Country'

# Cleaning spaces in 'Country' column
print(df['Country'].str.strip())  # Removes leading & trailing spaces
print(df['Country'].str.replace(' ', ''))  # Removes all spaces

# Corrected regex replace for 'Year' column
df['Year'] = df['Year'].str.replace(r'(?P<year>\d{4})\?', lambda m: m.group('year'), regex=True)

print(df)

'''
Breakdown of the Code:
----------------------
1. df['Year'].str.replace(...)
   - This applies the replace function on a string column (df['Year']).
   - The str.replace() function is used for string replacement in a Pandas Series.

2. r'(?P<year>\d{4})\?' (Regular Expression - Regex)
   - r'' → Raw string format for regex.
   - (?P<year>\d{4}) → Captures a 4-digit year (e.g., 1998, 2023) and assigns it a named group 'year'.
   - \? → Matches a literal question mark (?) after the year.

3. lambda m: m.group('year') (Replacement using a Lambda Function)
   - lambda m: m.group('year') extracts the captured year from the match (m).
   - m.group('year') returns only the year, effectively removing the '?'.
'''
