import numpy as np
import pandas as pd

df = pd.DataFrame({
    'Population': [35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.523],
    'GDP': [
        1785387,
        2833687,
        3874437,
        2167744,
        4602367,
        2950039,
        17348075
    ],
    'Surface Area': [
        9984670,
        640679,
        357114,
        301336,
        377930,
        242495,
        9525067
    ],
    'HDI': [
        0.913,
        0.888,
        0.916,
        0.873,
        0.891,
        0.907,
        0.915
    ],
    'Continent': [
        'America',
        'Europe',
        'Europe',
        'Europe',
        'Asia',
        'Europe',
        'America'
    ]
}, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])

print(df)

df.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]

print(df)
print(df.columns)
print(df.index)
print(df.info())
print(df.size)
print(df.shape)
print(df.describe())
print(df.dtypes)
print(df.dtypes.value_counts())

## Indexing, Selection and Slicing

# Individual columns in the DataFrame can be selected with regular indexing. Each column is represented as a `Series`:
print(df.loc['Canada'])
print(df.iloc[-1])
print(df['Population'])

# Note that the `index` of the returned Series is the same as the DataFrame one. And its `name` is the name of the column. If you're working on a notebook and want to see a more DataFrame-like format you can use the `to_frame` method:
print(df['Population'].to_frame())

# Multiple columns can also be selected similarly to `numpy` and `Series`:
# In this case, the result is another `DataFrame`. Slicing works differently, it acts at "row level", and can be counterintuitive:
print(df[1:3])

# Row level selection works better with `loc` and `iloc` **which are recommended** over regular "direct slicing" (`df[:]`).

# `loc` selects rows matching the given index:
print(df.loc['Italy'])
print(df.loc['France': 'Italy'])

# As a second "argument", you can pass the column(s) you'd like to select:
print(df.loc['France': 'Italy', 'Population'])
print(df.loc['France': 'Italy', ['Population', 'GDP']])

# `iloc` works with the (numeric) "position" of the index:
print(df.iloc[0])
print(df.iloc[-1])
print(df.iloc[[0, 1, -1]])
print(df.iloc[1:3, 3])
print(df.iloc[1:3, [0, 3]])
print(df.iloc[1:3, 1:3])

# > **RECOMMENDED: Always use `loc` and `iloc` to reduce ambiguity, especially with `DataFrame`s with numeric indexes.**

## Conditional selection (boolean arrays)

# We saw conditional selection applied to `Series` and it'll work in the same way for `DataFrame`s. After all, a `DataFrame` is a collection of `Series`:
print(df['Population'] > 70)
print(df.loc[df['Population'] > 70])
print(df.loc[df['Population'] > 70, 'Population'])
print(df.loc[df['Population'] > 70, ['Population', 'GDP']])

## Dropping stuff

# Opposed to the concept of selection, we have "dropping". Instead of pointing out which values you'd like to _select_ you could point which ones you'd like to `drop`:
print(df.drop(['Canada', 'Japan']))
print(df.drop(columns=['Population', 'HDI']))
print(df.drop(['Italy', 'Canada'], axis=0))
print(df.drop(['Population', 'HDI'], axis=1))
print(df.drop(['Population', 'HDI'], axis='columns'))
print(df.drop(['Canada', 'Germany'], axis='rows'))

# All these `drop` methods return a new `DataFrame`. If you'd like to modify it "in place", you can use the `inplace` attribute (there's an example below).

## Operations
print(df[['Population', 'GDP']] / 100)

# **Operations with Series** work at a column level, broadcasting down the rows (which can be counterintuitive).
crisis = pd.Series([-1_000_000, -0.3], index=['GDP', 'HDI'])
print(crisis)
print(df[['GDP', 'HDI']] + crisis)

## Modifying DataFrames

# It's simple and intuitive, You can add columns, or replace values for columns without issues:
### Adding a new column
langs = pd.Series(
    ['French', 'German', 'Italian'],
    index=['France', 'Germany', 'Italy'],
    name='Language'
)
print(langs)
df['Language'] = langs
print(df)

### Replacing values per column
df['Language'] = 'English'
print(df)

### Renaming Columns
df.rename(
    columns={
        'HDI': 'Human Development Index',
        'Anual Popcorn Consumption': 'APC'
    }, index={
        'United States': 'USA',
        'United Kingdom': 'UK',
        'Argentina': 'AR'
    })

print(df.rename(index=str.upper))
print(df.rename(index=lambda x: x.lower()))  # Lambda function is used to convert all index labels to lowercase.

### Dropping columns
df.drop(columns='Language', inplace=True)

### Adding values
df._append(pd.Series({
    'Population': 3,
    'GDP': 5
}, name='China'))

print(df)

df.loc['China'] = pd.Series({'Population': 1_400_000_000, 'Continent': 'Asia'})
print(df)

# We can use `drop` to just remove a row by index:
df.drop('China', inplace=True)
print(df)

### More radical index changes
df.reset_index()
df.set_index('Population')

## Creating columns from other columns

# Altering a DataFrame often involves combining different columns into another. For example, in our Countries analysis, we could try to calculate the "GDP per capita", which is just, `GDP / Population`.
print(df[['Population', 'GDP']])

# The regular pandas way of expressing that, is just dividing each series:
print(df['GDP'] / df['Population'])

# The result of that operation is just another series that you can add to the original `DataFrame`:
df['GDP Per Capita'] = df['GDP'] / df['Population']
print(df)

## Statistical info

# You've already seen the `describe` method, which gives you a good "summary" of the `DataFrame`. Let's explore other methods in more detail:
print(df.describe())

population = df['Population']  # Fixed the assignment
print(population)

print(population.min(), population.max())
print(population.sum())
print(population.sum() / len(population))
print(population.mean())
print(population.std())
print(population.median())
print(population.describe())

print(population.quantile(.25))  # Quantile function returns the value below which a given percentage of data falls.

print(population.quantile([.2, .4, .6, .8, 1]))  # This returns multiple quantile values at different percentages.
