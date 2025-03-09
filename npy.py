import numpy as np
import sys

# Creating NumPy arrays
print(np.array([1, 2, 3]))

a = np.array([1, 2, 3, 4, 5.12, 7.0, 'a'])
print(a[0], a[-1])
print(a[0:-1])
print(a[::2])

b = np.array([1, 2, 3])
print(b.dtype)
print(np.array([1, 2, 3, 4], dtype=float))

print(a.shape)  # Number of elements in brackets
print(a.ndim)  # Dimension
print(a.size)  # Total number of elements

# 3D Array
B = np.array([
    [
        [12, 11, 10],
        [9, 8, 7],
    ],
    [
        [6, 5, 4],
        [3, 2, 1]
    ]
])
print(B)
print(B.shape)  # (2,2,3)
print(B.ndim)  # 3D array
print(B.size)  # Total elements

# Square Matrix
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(A[1][0])
print(A[:, :2])
A[1] = np.array([10, 10, 10])
A[2] = 99
print(A)

# Summary statistics
a = np.array([1, 2, 3, 4])
print(a.sum())
print(a.mean())
print(a.std())
print(a.var())

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(A.sum())
print(A.mean())
print(A.std())
print(A.sum(axis=0))  # Column-wise sum
print(A.sum(axis=1))  # Row-wise sum

# Element-wise operations
a = np.arange(4)
print(a)
a += 10
print(a)
a *= 10
print(a)

# Boolean Indexing
a = np.array([0, 1, 2, 3])
print(a >= 2)
print(a[a > a.mean()])
print(a[(a <= 2) & (a % 2 == 0)])

# Matrix multiplication
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
B = np.array([
    [6, 5],
    [4, 3],
    [2, 1]
])
print(A @ B)
print(B.T @ A)

# Memory size comparison
print(sys.getsizeof(1))
print(sys.getsizeof(10**100))
print(np.dtype(int).itemsize)
print(np.dtype(np.int8).itemsize)
print(np.dtype(float).itemsize)
print(sys.getsizeof([1]))
print(np.array([1]).nbytes)

# Useful NumPy functions
print(np.random.random(size=2))
print(np.random.normal(size=2))
print(np.random.rand(2, 4))
print(np.arange(10))
print(np.arange(5, 10))
print(np.arange(0, 1, .1))
print(np.arange(10).reshape(2, 5))
print(np.arange(10).reshape(5, 2))
print(np.linspace(0, 1, 5))
print(np.linspace(0, 1, 20))
print(np.linspace(0, 1, 20, False))
print(np.zeros(5))
print(np.zeros((3, 3)))
print(np.zeros((3, 3), dtype=int))
print(np.ones(5))
print(np.ones((3, 3)))
print(np.empty(5))
print(np.empty((2, 2)))
print(np.identity(3))
print(np.eye(3, 3))
print(np.eye(8, 4))
print(np.eye(8, 4, k=1))
print(np.eye(8, 4, k=-3))
print("Hello World"[6])
