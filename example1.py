import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(
    'btc-eth-prices-outliers.csv',
    index_col=0,
    parse_dates=True
)
'''parse_dates=True means that Pandas will attempt to convert the index column (specified by index_col=0) into a datetime object.'''
print(df.head())
df.plot(figsize=(16, 9))
plt.show()
df.loc['2017-12': '2017-12-15'].plot(y='Ether', figsize=(16, 9))
plt.show()
df_na = df.loc['2017-12': '2017-12-15']
print(df_na)
print(df_na['Ether'].isna().values.any())
print(df_na.loc[df_na['Ether'].isna()])

print(df.loc['2017-12-06': '2017-12-12'])
print(df.loc['2017-12-06': '2017-12-12'].fillna(method='bfill'))
print(df.fillna(method='bfill', inplace=True))
df.plot(figsize=(16, 9))
plt.show()
df['2017-12-25':'2018-01-01'].plot()
plt.show()
df['2018-03-01': '2018-03-09'].plot()
plt.show()
df_cleaned = df.drop(pd.to_datetime(['2017-12-28', '2018-03-04']))
print(df_cleaned)
df_cleaned.plot(figsize=(16, 9))
plt.show()
  ##cleaning analysis
print(df.mean())
print(df_cleaned.mean())
print(df.median())
df_cleaned.plot(kind='hist', y='Ether', bins=150)
plt.show()
df_cleaned.plot(kind='hist', y='Bitcoin', bins=150)
plt.show()
fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Ether'], ax=ax)
plt.show()
fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], rug=True, ax=ax)
plt.show()
fig, ax = plt.subplots(figsize=(15, 7))
sns.kdeplot(df_cleaned['Ether'], shade=True, cut=0, ax=ax)
sns.rugplot(df_cleaned['Ether'], ax=ax)
plt.show()
fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))

plt.show()
fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax, bins=50,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))

plt.show()
sns.jointplot(x="Bitcoin", y="Ether", data=df_cleaned, size=9)
plt.show()
fig, ax = plt.subplots(figsize=(15, 7))
sns.regplot(x="Bitcoin", y="Ether", data=df_cleaned, ax=ax)
plt.show()
print(df_cleaned['Bitcoin'].quantile(.2))
fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax, bins=50,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
ax.axhline(0.2, color='red')
ax.axvline(df_cleaned['Bitcoin'].quantile(.2), color='red')
plt.show()
print(df_cleaned['Bitcoin'].quantile(.5))
print(df_cleaned['Bitcoin'].median())
fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax, bins=50,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
ax.axhline(0.5, color='red')
ax.axvline(df_cleaned['Bitcoin'].quantile(.5), color='red')
plt.show()
fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax, bins=50,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
ax.axhline(0.5, color='red')
ax.axvline(df_cleaned['Bitcoin'].median(), color='red')
plt.show()
'''## Dispersion

We'll use a few methods to measure dispersion in our dataset, most of them well known:

* Range
* Variance and Standard Deviation
* IQR'''
print(df['Bitcoin'].max() - df['Bitcoin'].min())
print(df_cleaned['Bitcoin'].max() - df_cleaned['Bitcoin'].min())
print(df['Bitcoin'].var())
print(df['Bitcoin'].std())
print(df_cleaned['Bitcoin'].std())
'''### IQR

The [Interquartile range]) is a good measure of "centered" dispersion, and is calculated as `Q3 - Q1` (3rd quartile - 1st quartile).'''
print(df['Bitcoin'].quantile(.75) - df['Bitcoin'].quantile(.25))

print(df_cleaned['Bitcoin'].quantile(.75) - df_cleaned['Bitcoin'].quantile(.25))
###### Using `std`: Z scores

#We can now define those values that are a couple of Z scores above or below the mean (or the max/min value). Example:
upper_limit = df['Bitcoin'].mean() + 2 * df['Bitcoin'].std()
lower_limit = df['Bitcoin'].mean() - 2 * df['Bitcoin'].std()
print("Upper Limit: {}".format(upper_limit))
print("Lower Limit: {}".format(lower_limit))
fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df['Bitcoin'], ax=ax)
ax.axvline(lower_limit, color='red')
ax.axvline(upper_limit, color='red')
plt.show()
##### Using IQRs

#We can use the IQR instead of std if we think that the standard deviation might be **too** affected by the outliers/invalid values.
iqr = df['Bitcoin'].quantile(.75) - df['Bitcoin'].quantile(.25)
print(iqr)
upper_limit = df['Bitcoin'].mean() + 2 * iqr
lower_limit = df['Bitcoin'].mean() - 2 * iqr
print("Upper Limit: {}".format(upper_limit))
print("Lower Limit: {}".format(lower_limit))
fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df['Bitcoin'], ax=ax)
ax.axvline(lower_limit, color='red')
ax.axvline(upper_limit, color='red')
plt.show()
### Cleaning invalid values analytically

#It's time now to remove these invalid values analytically, we'll use the upper limit defined by standard deviation:
upper_limit = df['Bitcoin'].mean() + 2 * df['Bitcoin'].std()
df[df['Bitcoin'] < upper_limit].plot(figsize=(16, 7))
plt.show()
df.drop(df[df['Bitcoin'] > upper_limit].index).plot(figsize=(16, 7))
plt.show()




