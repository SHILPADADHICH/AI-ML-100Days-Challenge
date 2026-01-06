## 1\. What is NumPy and why is it fast?

NumPy = Numerical Python

-   It provides a special data structure called ndarray (N‑dimensional array).
    
-   Designed for fast numerical computing: linear algebra, statistics, array operations, etc.
    
-   Almost every ML/DL library (Pandas, TensorFlow, PyTorch, etc.) relies on NumPy.
    

Why NumPy is faster than Python lists

1.  Fixed type & contiguous memory
    
    -   Python list: can hold mixed types, elements are pointers → scattered in memory → slower.
        
    -   NumPy array: all elements have the same dtype (e.g. `float64`), stored in contiguous memory → CPU can process them with vectorized instructions.
        
2.  Vectorization (no Python loops)
    
    -   Python list addition often needs `for` loops in Python (slow).
        
    -   NumPy uses optimized C code internally and can operate on whole arrays at once.
        

python

`# Python list lst = [1, 2, 3, 4] result = [x * 2 for x in lst] # NumPy array import numpy as np arr = np.array([1, 2, 3, 4]) result = arr * 2      # vectorized, no explicit loop`

3.  SIMD and BLAS/LAPACK
    
    -   NumPy uses low-level libraries (BLAS, LAPACK) and CPU vector instructions (SIMD) for matrix operations.
        

ndarray vs list

-   List: flexible, general-purpose container.
    
-   ndarray:
    
    -   Homogeneous data type.
        
    -   Efficient math operations: `+`, `*`, `**`, `sqrt`, matrix multiplication, etc.
        
    -   Supports dimensions: 1D (vector), 2D (matrix), 3D+ (tensors).
        

Installing & importing NumPy

bash

`pip install numpy`

python

`import numpy as np`

* * *

## 2\. Array creation

Know these by heart—they’re used everywhere.

python

`import numpy as np`

## `np.array()`

Convert Python list (or nested lists) to numpy array.

python

`a = np.array([1, 2, 3])          # 1D b = np.array([[1, 2], [3, 4]])   # 2D`

## `np.zeros()`

All zeros.

python

`z = np.zeros((3, 4))   # 3 rows, 4 cols of 0.0`

## `np.ones()`

All ones.

python

`o = np.ones((2, 3))    # 2x3 matrix of 1.0`

## `np.full()`

Array filled with a specific value.

python

`f = np.full((3, 4), 7)   # 3x4 all 7`

## `np.eye()`

Identity matrix: 1s on diagonal, 0 elsewhere.

python

`I = np.eye(5)      # 5x5 identity`

## `np.arange()`

Like Python `range`, but returns an array.

python

`r = np.arange(0, 10, 2)   # [0, 2, 4, 6, 8]`

## `np.linspace()`

Evenly spaced values between start and end (including end).

python

`l = np.linspace(0, 1, 5)  # [0. , 0.25, 0.5 , 0.75, 1. ]`

## `np.random.rand()`

Random floats in \[0,1)\[0,1) from a uniform distribution.

python

`u = np.random.rand(2, 3)   # shape (2,3)`

## `np.random.randint()`

Random integers from low (inclusive) to high (exclusive).

python

`ri = np.random.randint(1, 101, size=(4, 4))  # 1..100, shape (4,4)`

* * *

## 3\. Array properties

For an array `arr`:

python

`arr = np.array([[1, 2, 3],                 [4, 5, 6]])`

-   `arr.ndim` → number of dimensions
    
    -   Here: 22 (2D array / matrix).
        
-   `arr.shape` → tuple describing size in each dimension
    
    -   Here: `(2, 3)` (2 rows, 3 columns).
        
-   `arr.size` → total number of elements
    
    -   Here: 2×3\=62×3\=6.
        
-   `arr.dtype` → data type of elements
    
    -   e.g. `int64`, `float64`, `bool`.
        

You can cast type:

python

`arr_float = arr.astype(float)`

* * *

## 4\. Indexing & slicing

Exactly like Python lists, but extended to multiple dimensions.

## 1D indexing & slicing

python

`a = np.array([10, 20, 30, 40, 50]) a[0]        # 10 a[-1]       # 50 a[1:4]      # [20 30 40] a[::-1]     # reverse: [50 40 30 20 10]`

## 2D indexing

python

`m = np.array([[1, 2, 3],               [4, 5, 6],              [7, 8, 9]]) m[0, 0]     # 1 (row 0, col 0) m[1, 2]     # 6 (row 1, col 2)`

## Row & column selection

python

`m[1, :]     # second row => [4 5 6] m[:, 2]     # third column => [3 6 9]`

## 2D slicing / sub‑matrix

python

`m[0:2, 1:3]   # rows 0–1, cols 1–2 => [[2 3],               #                       [5 6]]`

## Boolean indexing

Create a boolean mask and use it to filter values.

python

`a = np.array([1, 2, 3, 4, 5, 6]) mask = a > 3               # [False False False  True  True  True] a[mask]                    # [4 5 6] # directly a[a % 2 == 0]              # even numbers`

Very powerful for conditions in ML (e.g. filtering rows, thresholding).

* * *

## 5\. Mathematical operations

All operations are element‑wise by default.

python

`a = np.array([1, 2, 3]) b = np.array([10, 20, 30]) a + b       # [11 22 33] a - b       # [-9 -18 -27] a * b       # [10 40 90] a / b       # [0.1 0.1 0.1] a ** 2      # [1 4 9] a + 5       # [6 7 8] (scalar added to all elements)`

## Universal functions (ufuncs)

Vectorized functions that act on each element.

python

`np.sqrt(a)           # square root np.log(a)            # natural log np.exp(a)            # e^a np.sin(a), np.cos(a) np.abs(a)`

These are much faster than looping and using `math` module.

* * *

## 6\. Aggregations

Operations that reduce an array to a single value or along an axis.

python

`m = np.array([[1, 2, 3],               [4, 5, 6]])`

Basic aggregations:

python

`m.sum()      # 1+2+3+4+5+6 = 21 m.mean()     # 21/6 = 3.5 m.max()      # 6 m.min()      # 1 m.std()      # standard deviation`

## `axis=0` vs `axis=1`

-   `axis` tells along which dimension to aggregate.
    

For 2D array with shape `(rows, cols)`:

-   `axis=0` → collapse rows, operate down columns → result has one value per column.
    
-   `axis=1` → collapse columns, operate across rows → result has one value per row.
    

python

`m.sum(axis=0)    # column-wise sum: [1+4, 2+5, 3+6] -> [5 7 9] m.sum(axis=1)    # row-wise sum:   [1+2+3, 4+5+6] -> [6 15]`

In ML, `axis` is crucial for operations like feature-wise normalization, batch-wise calculations, etc.

* * *

## 7\. Broadcasting

Broadcasting = automatic expansion of arrays with different shapes to make element‑wise operations possible, without actually copying data.

Rules (simplified):

1.  Compare shapes from right to left.
    
2.  Two dimensions are compatible if:
    
    -   they are equal, or
        
    -   one of them is 11.
        
3.  If one array has fewer dimensions, prepend 1s.
    

Example:

python

`A = np.array([[1, 2, 3],               [4, 5, 6]])      # shape (2, 3) b = np.array([10, 20, 30])     # shape (3,)`

Comparison:

-   AA: (2,3)(2,3)
    
-   bb: (3)(3) → treat as (1,3)(1,3)
    

From right:

-   33 vs 33 → OK
    
-   22 vs 11 → 11 can broadcast to 22
    

So `A + b` is valid:

python

`A + b # [[11 22 33], #  [14 25 36]]`

Another example:

python

`v = np.array([[1],               [2],              [3]])      # shape (3,1) B = np.array([10, 20, 30])     # shape (3,) ~ (1,3) # v shape (3,1), B shape (1,3) -> result shape (3,3) v + B # [[11 21 31], #  [12 22 32], #  [13 23 33]]`

Broadcasting appears everywhere in ML: adding bias terms, normalizing columns, etc.

* * *

## 8\. Shape manipulation

You must be very comfortable with reshaping for ML models.

Assume:

python

`a = np.arange(12)       # [0..11], shape (12,)`

## `reshape()`

Change shape without changing data.

python

`m = a.reshape(3, 4)   # shape (3,4) # [[0 1 2 3], #  [4 5 6 7], #  [8 9 10 11]]`

You can use `-1` to let NumPy infer that dimension:

python

`a.reshape(2, -1)   # shape (2, 6) a.reshape(-1, 3)   # shape (4, 3)`

## `flatten()` vs `ravel()`

Both convert to 1D, but:

-   `flatten()` → returns a copy.
    
-   `ravel()` → returns a view if possible.
    

python

`b = m.flatten()    # new independent array c = m.ravel()      # view: linked to m if possible`

If you modify `c`, it may modify `m` (because same underlying data).

## `transpose()`

Swap axes. For 2D, just rows ↔ columns.

python

`mt = m.T          # or m.transpose() # shape (4,3)`

For multi‑dim, you can specify axes:

python

`x = np.random.rand(2, 3, 4)   # (batch, height, width) x2 = np.transpose(x, (0, 2, 1))  # reorder axes`

* * *

## 9\. Copy vs view

NumPy often returns views (slices) instead of copies for efficiency.

python

`a = np.array([1, 2, 3, 4, 5]) b = a[1:4]          # view: b = [2, 3, 4] b[0] = 99 a                  # [1, 99, 3, 4, 5]  a changed!`

If you want an independent array:

python

`c = a[1:4].copy() c[0] = 100 a                  # unchanged now`

Remember: view shares data → changes reflect in original; copy has its own data → safe but uses more memory.

* * *

## 10\. Explaining the practice questions logically

I won’t dump code for all 50 (it would be huge), but I’ll tell you the pattern to solve them and the important idea behind each group. You can implement them easily in a notebook.

## Level 1: Basics (1–15)

Concepts used:

-   Creation: `np.array`, `np.zeros`, `np.ones`, `np.full`, `np.eye`, `np.arange`, `np.linspace`, `np.random.rand`, `np.random.randint`, `np.empty`
    
-   Properties: `shape`, `size`, `dtype`, `ndim`
    
-   Type conversion: `astype`
    
-   Boolean arrays: `astype(bool)` or comparisons
    
-   Total elements: `rows * cols` or `.size`
    

Typical patterns:

python

`# 1: 1..10 arr = np.arange(1, 11) # 2: zeros (3,3) z = np.zeros((3, 3)) # 3: full of 7, 3x4 f = np.full((3, 4), 7) # 4: identity 5x5 I = np.eye(5) # 5: 10 evenly spaced between 0 and 1 lin = np.linspace(0, 1, 10) # 6: props a = np.array([5, 10, 15, 20, 25]) a.shape, a.size, a.dtype # 7: list to array a = np.array([1, 2, 3, 4]) # 8: arange with step 2 ar = np.arange(0, 21, 2) # 9: random (2,3) between 0 and 1 r = np.random.rand(2, 3) # 10: random ints ri = np.random.randint(1, 101, size=(4, 4)) # 11: .ndim for 3D x = np.zeros((2, 3, 4)) x.ndim   # 3 # 12: int to float a = np.array([1, 2, 3]) a_float = a.astype(float) # 13: boolean array from [1, 0, 3, 0] b = np.array([1, 0, 3, 0], dtype=bool) # 14: total in (5,6) np.zeros((5, 6)).size   # or 5*6 # 15: empty (uninitialized content) e = np.empty((3, 3))`

## Level 2: Indexing & slicing (16–25)

Concepts used:

-   1D slicing (`a[:3]`, `a[-1]`, reverse `a[::-1]`)
    
-   2D slicing (`m[:, -1]`, `m[1, :]`, `m[0:2, 0:2]`)
    
-   Boolean masks (`a > 10`, `a % 2 == 0`)
    
-   In‑place assignment
    

Examples:

python

`# 16: first three a[:3] # 17: last column m[:, -1] # 18: second row m[1, :] # 19: 2x2 sub-matrix (e.g. top-left) m[0:2, 0:2] # 20: reverse a[::-1] # 21: replace 3rd element with 99 a[2] = 99 # 22: >10 a[a > 10] # 23: even to 0 a[a % 2 == 0] = 0 # 24: divisible by 3 a[a % 3 == 0] # 25: count > mean mean_val = a.mean() count = (a > mean_val).sum()`

## Level 3: Math & aggregations (26–35)

Concepts:

-   Element‑wise operations (`+`, `*`, ufuncs)
    
-   Aggregations (`sum`, `mean`, `max`, `std`)
    
-   Normalization: scale array between 0 and 1
    
-   `np.argmax` for index of max
    
-   Dot product: `np.dot` or `@`
    

Examples:

python

`# 26: element-wise add c = a + b # 27: scalar multiply b = a * 5 # 28: sqrt np.sqrt(a) # 29: sum all in matrix m.sum() # 30: mean of each column m.mean(axis=0) # 31: max in each row m.max(axis=1) # 32: std a.std() # 33: normalize 0–1 x_min = a.min() x_max = a.max() norm = (a - x_min) / (x_max - x_min) # 34: index of max idx = np.argmax(a) # 35: dot product v1 = np.array([1, 2, 3]) v2 = np.array([4, 5, 6]) dot = np.dot(v1, v2)    # or v1 @ v2`

## Level 4: Shape & broadcasting (36–45)

Concepts:

-   `reshape`, `flatten`, `ravel`, `transpose`
    
-   `np.vstack`, `np.hstack`
    
-   Broadcasting for vector + matrix
    
-   Multiply per column/row using broadcasting
    
-   `reshape` or `reshape(-1, ...)` to reduce dimensions
    
-   Shape comparison via `.shape`
    

Examples:

python

`# 36: reshape a = np.arange(12) m = a.reshape(3, 4) # 37: flatten flat = m.flatten() # 38: transpose mt = m.T # 39: vertical stack a1 = np.array([1, 2, 3]) a2 = np.array([4, 5, 6]) v = np.vstack((a1, a2)) # 40: horizontal stack h = np.hstack((a1, a2)) # 41: broadcasting add [1,2,3] M = np.array([[10, 20, 30],               [40, 50, 60]]) v = np.array([1, 2, 3]) res = M + v # 42: subtract mean from every element mean_val = a.mean() centered = a - mean_val # 43: multiply each column by vector M = np.array([[1, 2, 3],               [4, 5, 6]]) col_factors = np.array([1, 10, 100])   # shape (3,) M_scaled = M * col_factors   # broadcast across rows # 44: 3D to 2D x = np.random.rand(2, 3, 4)   # e.g. x2d = x.reshape(2, -1)        # or (-1, 4) depending on need # 45: same shape? A.shape == B.shape`

## Level 5: ML-style operations (46–50)

Concepts:

-   Clipping / thresholding
    
-   `np.where` (vectorized if‑else)
    
-   `np.unique(return_counts=True)`
    
-   Sorting with `np.sort` and `axis`
    
-   Mean normalization: (x−mean)/std(x−mean)/std
    

Examples:

python

`# 46: negatives to 0 a[a < 0] = 0 # 47: label >50 as 1 else 0 labels = np.where(a > 50, 1, 0) # 48: unique + counts vals, counts = np.unique(a, return_counts=True) # 49: sort row-wise sorted_rows = np.sort(M, axis=1) # 50: mean normalization mean = a.mean() std = a.std() norm = (a - mean) / std`

* * *

## 11\. Challenge: doing NumPy things with pure Python

The idea is to understand what NumPy is abstracting away.

## Element-wise list addition

python

`def list_add(a, b):     assert len(a) == len(b)    return [x + y for x, y in zip(a, b)] a = [1, 2, 3] b = [4, 5, 6] list_add(a, b)   # [5, 7, 9]`

## Mean calculation

python

`def mean(lst):     return sum(lst) / len(lst) mean([1, 2, 3, 4])   # 2.5`

## Matrix addition using loops

python

`def mat_add(A, B):     rows = len(A)    cols = len(A[0])    result = []    for i in range(rows):        row = []        for j in range(cols):            row.append(A[i][j] + B[i][j])        result.append(row)    return result A = [[1, 2], [3, 4]] B = [[5, 6], [7, 8]] mat_add(A, B) # [[6, 8], #  [10, 12]]`

NumPy does all of this in C, vectorized and optimized.