### 🧠 Why NumPy?

Python lists are:

Slow

Memory inefficient

Not designed for math

NumPy:

### ⚡ Very fast (written in C)

### 📦 Memory efficient

### 🧮 Designed for numerical computing

❤️ Core of AI/ML

### 🔹 1. NumPy Arrays (ndarray)
What is an ndarray?

A NumPy array is:

Homogeneous (same data type)

Fixed size

Multi-dimensional

```python
import numpy as np

```
Create array from list
```python
a = np.array([1, 2, 3, 4])
print(a)

```
### 📌 Difference from list:

a + 2     # works
# [3 4 5 6]

But in list:

[1,2,3] + 2   # ❌ error

Array Types (Dimensions)
Type	Shape
1D	[1,2,3]
2D	[[1,2],[3,4]]
3D	[[[...]]]
```python
arr2d = np.array([[1,2],[3,4]])

```
### 🔹 2. Array Attributes (VERY IMPORTANT)
```python
arr = np.array([[1,2,3],[4,5,6]])

```
Attribute	Meaning
arr.ndim	number of dimensions
arr.shape	rows × columns
arr.size	total elements
arr.dtype	data type
```python
print(arr.ndim)    # 2
print(arr.shape)   # (2,3)
print(arr.size)    # 6
print(arr.dtype)   # int32/int64

```
### 🔹 3. Array Creation Methods (MUST KNOW)
zeros
np.zeros((3,3))

ones
np.ones((2,4))

full
np.full((2,2), 7)

identity matrix
np.eye(3)

range
np.arange(1, 10, 2)   # start, stop, step

linspace (VERY IMPORTANT FOR ML)
np.linspace(0, 1, 5)
# evenly spaced values

random
np.random.rand(3,3)     # 0–1
np.random.randint(1,10,(3,3))

### 🔹 4. Indexing & Slicing (Hands-on part)
1D slicing
```python
a = np.array([10,20,30,40,50])
```
a[1:4]    # [20 30 40]

2D indexing
```python
arr = np.array([[1,2,3],[4,5,6]])

```
arr[0,1]     # 2
arr[:,1]     # column
arr[1,:]     # row

Boolean indexing (VERY IMPORTANT)
arr[arr > 3]

Used heavily in ML filtering

### 🔹 5. Mathematical Operations (Core Power)
Element-wise operations
```python
a = np.array([1,2,3])
b = np.array([4,5,6])

```
a + b
a - b
a * b
a / b

Scalar operations
a * 10

Universal Functions (ufuncs)
np.sqrt(a)
np.log(a)
np.exp(a)
np.sin(a)

### 🔹 6. Aggregation Functions
```python
arr = np.array([[1,2,3],[4,5,6]])

```
Function	Example
sum	np.sum(arr)
mean	np.mean(arr)
max	np.max(arr)
min	np.min(arr)
std	np.std(arr)
Axis concept (VERY IMPORTANT)
np.sum(arr, axis=0)  # column-wise
np.sum(arr, axis=1)  # row-wise

### 🔹 7. Broadcasting (MOST IMPORTANT CONCEPT 🔥)
What is Broadcasting?

NumPy automatically expands smaller arrays to match larger ones.

Example
```python
arr = np.array([[1,2,3],[4,5,6]])
```
arr + 10

Vector + Matrix
```python
v = np.array([1,2,3])
```
arr + v

Rules:

Dimensions must be equal OR

One of them must be 1

This is why NumPy is fast for ML math.

### 🔹 8. Reshaping & Manipulating Arrays
```python
a = np.arange(6)
```
a.reshape(2,3)

a.flatten()
a.ravel()

np.transpose(arr)
arr.T

### 🔹 9. Copy vs View (VERY IMPORTANT FOR BUGS)
```python
a = np.array([1,2,3])
b = a
b[0] = 99
print(a)   # changed ❌

```
Correct way
```python
b = a.copy()

```
### 🔹 10. Replicate NumPy using Native Python (Challenge)
NumPy-style addition
```python
a = [1,2,3]
b = [4,5,6]

result = []
for i in range(len(a)):
```
result.append(a[i] + b[i])

Mean without NumPy
```python
def mean(arr):
    return sum(arr) / len(arr)

```
Matrix addition
```python
A = [[1,2],[3,4]]
B = [[5,6],[7,8]]

C = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
```
row.append(A[i][j] + B[i][j])
C.append(row)

### 👉 This shows why NumPy exists.

### 🔹 11. 50+ NumPy Operations You Should Practice

- ✔ array creation
- ✔ slicing
- ✔ reshaping
- ✔ arithmetic
- ✔ comparison
- ✔ boolean indexing
- ✔ aggregations
- ✔ transpose
- ✔ random
- ✔ broadcasting
- ✔ sorting
- ✔ unique
- ✔ where
- ✔ clip

Example:

np.where(arr > 3, 1, 0)
np.unique(arr)
np.sort(arr)

### 🧠 What You MUST Remember for AI/ML

✅ ndarray
✅ shape, ndim, axis
✅ broadcasting
✅ vectorized operations
✅ boolean indexing
✅ aggregation functions

### 📌 Day 4 Output Goal (Checklist)

- ✔ You can replace loops with NumPy
- ✔ You understand broadcasting
- ✔ You can slice & filter arrays
- ✔ You feel Python lists are slow 😄