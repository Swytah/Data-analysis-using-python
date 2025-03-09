import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('sakila.db')

df = pd.read_sql('''
    SELECT
        rental.rental_id, rental.rental_date, rental.return_date,
        customer.last_name AS customer_lastname,
        store.store_id,
        city.city AS rental_store_city,
        film.title AS film_title, film.rental_duration AS film_rental_duration,
        film.rental_rate AS film_rental_rate, film.replacement_cost AS film_replacement_cost,
        film.rating AS film_rating
    FROM rental
    INNER JOIN customer ON rental.customer_id == customer.customer_id
    INNER JOIN inventory ON rental.inventory_id == inventory.inventory_id
    INNER JOIN store ON inventory.store_id == store.store_id
    INNER JOIN address ON store.address_id == address.address_id
    INNER JOIN city ON address.city_id == city.city_id
    INNER JOIN film ON inventory.film_id == film.film_id
    ;
''', conn, index_col='rental_id', parse_dates=['rental_date', 'return_date'])
'''pd.read_sql(query, conn): Runs the SQL query and loads the results into a Pandas DataFrame (df).
index_col='rental_id': Sets the rental_id as the index of the DataFrame.
parse_dates=['rental_date', 'return_date']: Converts rental_date and return_date columns into datetime format.'''
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

## Numerical analysis and visualization

# We'll analyze the `film_rental_rate` column:
print(df['film_rental_rate'].describe())
print(df['film_rental_rate'].mean())
print(df['film_rental_rate'].median())
df['film_rental_rate'].plot(kind='box', vert=False, figsize=(14,6))
plt.show()
df['film_rental_rate'].plot(kind='density', figsize=(14,6)) # kde
plt.show()
ax = df['film_rental_rate'].value_counts().plot(kind='bar', figsize=(14,6))
ax.set_ylabel('Number of Rentals')
plt.show()

## Categorical analysis and visualization

# We'll analyze the `rental_store_city` column:
print(df['rental_store_city'].value_counts())
df['rental_store_city'].value_counts().plot(kind='pie', figsize=(6,6))
plt.show()
ax = df['rental_store_city'].value_counts().plot(kind='bar', figsize=(14,6))
ax.set_ylabel('Number of Rentals')
plt.show()

## Column wrangling

# We can also create new columns or modify existing ones.

### Add and calculate a new `rental_rate_return` column

# We want to know the rental rate of return of each film. To do that we'll use this formula:

# rental_gain_return = film_rental_rate / film_replacement_cost * 100

df['rental_gain_return'] = df['film_rental_rate'] / df['film_replacement_cost'] * 100

print(df['rental_gain_return'].head())
df['rental_gain_return'].plot(kind='density', figsize=(14,6))
plt.show()
print(df['rental_gain_return'].mean().round(2))
print(df['rental_gain_return'].median().round(2))
ax = df['rental_gain_return'].plot(kind='density', figsize=(14,6)) # kde
ax.axvline(df['rental_gain_return'].mean(), color='red')
ax.axvline(df['rental_gain_return'].median(), color='green')
plt.show()

# Each rental represents 13.6% of film cost.
# So 7.35 rentals are needed to recover film market price (film_replacement_cost)
print(100 / 13.6)
# While in average each film is rented 16.74 times.
print(df['film_title'].value_counts().mean())

## Selection & Indexing:
### Get the rental records of the customer with lastname `HANSEN`
print(df.loc[df['customer_lastname'] == 'HANSEN'])
### Create a list of all the films with the highest replacement cost
print(df['film_replacement_cost'].max())
print(df.loc[df['film_replacement_cost'] == df['film_replacement_cost'].max(), 'film_title'].unique())
### How many `PG` or `PG-13` rating films were rented?
print(df.loc[(df['film_rating'] == 'PG') | (df['film_rating'] == 'PG-13')].shape[0])
