import numpy as np
import pandas as pd
#What does "missing data" mean? What is a missing value? It depends on the origin of the data and the context it was generated. For example, for a survey, a _`Salary`_ field with an empty value, or a number 0, or an invalid value (a string for example) can be considered "missing data". These concepts are related to the values that Python will consider "Falsy":
falsy_values = (0, False, None, '', [], {})
#For Python, all the values above are considered "falsy":
any(falsy_values)
#Numpy has a special "nullable" value for numbers which is `np.nan`. It's _NaN_: "Not a number"
print(np.nan)
#The `np.nan` value is kind of a virus. Everything that it touches becomes `np.nan`:
print(3 + np.nan)
a = np.array([1, 2, 3, np.nan, np.nan, 4])
print(a.sum())
print(a.mean())
#This is better than regular `None` values, which in the previous examples would have raised an exception:
#print(3 + None)
#For a numeric array, the `None` value is replaced by `np.nan`:
a = np.array([1, 2, 3, np.nan, None, 4])
print(a)
#As we said, `np.nan` is like a virus. If you have any `nan` value in an array and you try to perform an operation on it, you'll get unexpected results:
a = np.array([1, 2, 3, np.nan, np.nan, 4])
print(a.mean())
print(a.sum())
#Numpy also supports an "Infinite" type:
print(np.inf)
#Which also behaves as a virus:
print(3 + np.inf)
print(np.inf / 3)
print(np.inf / np.inf)
b = np.array([1, 2, 3, np.inf, np.nan, 4])
print(b.sum())

### Checking for `nan` or `inf`

#There are two functions: `np.isnan` and `np.isinf` that will perform the desired checks:
print(np.isnan(np.nan))
print(np.isinf(np.inf))
#And the joint operation can be performed with `np.isfinite`.
print(np.isfinite(np.nan), np.isfinite(np.inf))
#`np.isnan` and `np.isinf` also take arrays as inputs, and return boolean arrays as results:
print(np.isnan(np.array([1, 2, 3, np.nan, np.inf, 4])))
print(np.isinf(np.array([1, 2, 3, np.nan, np.inf, 4])))
print(np.isfinite(np.array([1, 2, 3, np.nan, np.inf, 4])))
'''np.isinf(x) → Checks for Infinity (±∞)
Returns True if the value is positive or negative infinity (+∞, -∞), otherwise False.
np.isnan(x) → Checks for NaN (Not a Number)
Returns True if the value is NaN (Not a Number), otherwise False
np.isfinite(x) → Checks for Finite Values
Returns True if the value is not NaN or infinity (+∞, -∞), meaning it is a finite number'''
#_Note: It's not so common to find infinite values. From now on, we'll keep working with only `np.nan`_

### Filtering them out

#Whenever you're trying to perform an operation with a Numpy array and you know there might be missing values, you'll need to filter them out before proceeding, to avoid `nan` propagation. We'll use a combination of the previous `np.isnan` + boolean arrays for this purpose:
a = np.array([1, 2, 3, np.nan, np.nan, 4])
print(a[~np.isnan(a)])
#Which is equivalent to:
print(a[np.isfinite(a)])
#And with that result, all the operation can be now performed:
print(a[np.isfinite(a)].sum())
print(a[np.isfinite(a)].mean())










