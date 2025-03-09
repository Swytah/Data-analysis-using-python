import pandas as pd
import numpy as np
## Pandas Series
#We'll start analyzing "[The Group of Seven](https://en.wikipedia.org/wiki/Group_of_Seven)". Which is a political formed by Canada, France, Germany, Italy, Japan, the United Kingdom and the United States. We'll start by analyzing population, and for that, we'll use a `pandas.Series` object.
# In millions
g7_pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])
print(g7_pop)
#Someone might not know we're representing population in millions of inhabitants. Series can have a `name`, to better document the purpose of the Series:
g7_pop.name = 'G7 Population in millions'
print(g7_pop)
print(g7_pop.dtype)
print(g7_pop.values)
#They're actually backed by numpy arrays:
print(type(g7_pop.values))
#And they _look_ like simple Python lists or Numpy Arrays. But they're actually more similar to Python `dict`s.

#A Series has an `index`, that's similar to the automatic index assigned to Python's lists:
print(g7_pop)
print(g7_pop[0])
print(g7_pop.index)
l = ['a', 'b', 'c']
#But, in contrast to lists, we can explicitly define the index:
g7_pop.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]
print(g7_pop)
q=pd.Series({
    'Canada': 35.467,
    'France': 63.951,
    'Germany': 80.94,
    'Italy': 60.665,
    'Japan': 127.061,
    'United Kingdom': 64.511,
    'United States': 318.523
}, name='G7 Population in millions')
print(q)
e=pd.Series(
    [35.467, 63.951, 80.94, 60.665, 127.061, 64.511, 318.523],
    index=['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom',
       'United States'],
    name='G7 Population in millions')
print(e)
#You can also create Series out of other series, specifying indexes:
o=pd.Series(g7_pop, index=['France', 'Germany', 'Italy', 'Spain'])
print(o)

## Indexing

#Indexing works similarly to lists and dictionaries, you use the **index** of the element you're looking for:
print(g7_pop)
print(g7_pop['Canada'])
#Numeric positions can also be used, with the `iloc` attribute:
print(g7_pop.iloc[0])
print(g7_pop.iloc[-1])
#Selecting multiple elements at once:
print(g7_pop[['Italy', 'France']])
#(The result is another Series)
print(g7_pop.iloc[[0, 1]])
#Slicing also works, but important, in Pandas, the upper limit is also included:
print(g7_pop['Canada': 'Italy'])

## Conditional selection (boolean arrays)

#The same boolean array techniques we saw applied to numpy arrays can be used for Pandas `Series`:
print(g7_pop > 70)
print(g7_pop[g7_pop > 70])
print(g7_pop.mean())
print(g7_pop[g7_pop > g7_pop.mean()])
print(g7_pop.std())
print(g7_pop[(g7_pop > g7_pop.mean() - g7_pop.std() / 2) | (g7_pop > g7_pop.mean() + g7_pop.std() / 2)])

## Operations and methods
#Series also support vectorized operations and aggregation functions as Numpy:
print(g7_pop * 1_000_000)
print(g7_pop.mean())
print(np.log(g7_pop))
print(g7_pop['France': 'Italy'].mean())

## Boolean arrays
#(Work in the same way as numpy)
print(g7_pop > 80)
print(g7_pop[g7_pop > 80])
print(g7_pop[(g7_pop > 80) | (g7_pop < 40)])
print(g7_pop[(g7_pop > 80) & (g7_pop < 200)])

## Modifying series
g7_pop['Canada'] = 40.5
print(g7_pop)
g7_pop.iloc[-1] = 500
print(g7_pop)
g7_pop[g7_pop < 70] = 99.99
print(g7_pop)
