import numpy as np
import pandas as pd

### Pandas utility functions

# Similarly to `numpy`, pandas also has a few utility functions to identify and detect null values:
print(pd.isnull(np.nan))
print(pd.isnull(None))
print(pd.isna(np.nan))
print(pd.isna(None))

# The opposite ones also exist:
print(pd.notnull(None))
print(pd.notnull(np.nan))
print(pd.notna(np.nan))
print(pd.notnull(3))

# These functions also work with Series and `DataFrame`s:
print(pd.isnull(pd.Series([1, np.nan, 7])))
print(pd.notnull(pd.Series([1, np.nan, 7])))
print(pd.isnull(pd.DataFrame({
    'Column A': [1, np.nan, 7],
    'Column B': [np.nan, 2, 3],
    'Column C': [np.nan, 2, np.nan]
})))

### Pandas Operations with Missing Values

# Pandas manages missing values more gracefully than numpy. `nan`s will no longer behave as "viruses", and operations will just ignore them completely:
print(pd.Series([1, 2, np.nan]).count())
print(pd.Series([1, 2, np.nan]).sum())
print(pd.Series([2, 2, np.nan]).mean())

### Filtering missing data

# As we saw with numpy, we could combine boolean selection + `pd.isnull` to filter out those `nan`s and null values:
s = pd.Series([1, 2, 3, np.nan, np.nan, 4])
print(pd.notnull(s))
print(pd.isnull(s))
print(pd.notnull(s).sum())
print(pd.isnull(s).sum())
print(s[pd.notnull(s)])

# But both `notnull` and `isnull` are also methods of `Series` and `DataFrame`s, so we could use it that way:
print(s.isnull())
print(s.notnull())
print(s[s.notnull()])

### Dropping null values

# Boolean selection + `notnull()` seems a little bit verbose and repetitive. And as we said before: any repetitive task will probably have a better, more DRY way. In this case, we can use the `dropna` method:
print(s)
print(s.dropna())

### Dropping null values on DataFrames

# You saw how simple it is to drop `na`s with a Series. But with `DataFrame`s, there will be a few more things to consider, because you can't drop single values. You can only drop entire columns or rows. Let's start with a sample `DataFrame`:
df = pd.DataFrame({
    'Column A': [1, np.nan, 30, np.nan],
    'Column B': [2, 8, 31, np.nan],
    'Column C': [np.nan, 9, 32, 100],
    'Column D': [5, 8, 34, 110],
})
print(df)
print(df.shape)
print(df.info())
print(df.isnull())
print(df.isnull().sum())

# The default `dropna` behavior will drop all the rows in which _any_ null value is present:
print(df.dropna())

# In this case we're dropping **rows**. Rows containing null values are dropped from the DF. You can also use the `axis` parameter to drop columns containing null values:
print(df.dropna(axis=1))  # axis='columns' also works

# In this case, any row or column that contains **at least** one null value will be dropped. Which can be, depending on the case, too extreme. You can control this behavior with the `how` parameter. Can be either `'any'` or `'all'`:
df2 = pd.DataFrame({
    'Column A': [1, np.nan, 30],
    'Column B': [2, np.nan, 31],
    'Column C': [np.nan, np.nan, 100]
})
print(df2)
print(df.dropna(how='all'))
print(df.dropna(how='any'))  # default behavior

# You can also use the `thresh` parameter to indicate a _threshold_ (a minimum number) of non-null values for the row/column to be kept:
print(df)
print(df.dropna(thresh=3))
print(df.dropna(thresh=3, axis='columns'))

### Filling null values

print(s)

# **Filling nulls with an arbitrary value**
print(s.fillna(0))
print(s.fillna(s.mean()))
print(s)

# **Filling nulls with contiguous (close) values**

# The `method` argument is used to fill null values with other values close to that null one:
print(s.fillna(method='ffill'))
print(s.fillna(method='bfill'))

# This can still leave null values at the extremes of the Series/DataFrame:
print(pd.Series([np.nan, 3, np.nan, 9]).fillna(method='ffill'))
print(pd.Series([1, np.nan, 3, np.nan, np.nan]).fillna(method='bfill'))

### Filling null values on DataFrames

print(df)
print(df.fillna({'Column A': 0, 'Column B': 99, 'Column C': df['Column C'].mean()}))
print(df.fillna(method='ffill', axis=0))
print(df.fillna(method='ffill', axis=1))

### Checking if there are NAs

# The question is: Does this `Series` or `DataFrame` contain any missing value? The answer should be yes or no: `True` or `False`. How can you verify it?

# **Example 1: Checking the length**

# If there are missing values, `s.dropna()` will have fewer elements than `s`:
print(s.dropna().count())
missing_values = len(s.dropna()) != len(s)
print(missing_values)

# There's also a `count` method, that excludes `nan`s from its result:
print(len(s))
print(s.count())

# So we could just do:
missing_values = s.count() != len(s)
print(missing_values)

# **More Pythonic solution using `any`**

# The methods `any` and `all` check if either there's `any` True value in a Series or `all` the values are `True`. They work in the same way as in Python:
print(pd.Series([True, False, False]).any())
print(pd.Series([True, False, False]).all())
print(pd.Series([True, True, True]).all())

# The `isnull()` method returned a Boolean `Series` with `True` values wherever there was a `nan`:
print(s.isnull())

# So we can just use the `any` method with the boolean array returned:
print(pd.Series([1, np.nan]).isnull().any())
print(pd.Series([1, 2]).isnull().any())
print(s.isnull().any())

# A more strict version would check only the `values` of the Series:
print(s.isnull().values)
print(s.isnull().values.any())
