# Level 2: Indexing & slicing (16–25)
# Concepts used:

# 1D slicing (a[:3], a[-1], reverse a[::-1])

# 2D slicing (m[:, -1], m[1, :], m[0:2, 0:2])

# Boolean masks (a > 10, a % 2 == 0)

# In‑place assignment
import numpy as np
a = np.array([5, 10, 15, 20, 25])

m = np.array([[1, 2, 3],
              [4, 5, 6],])
# 16: first three
a[:3]

# 17: last column
m[:, -1]

# 18: second row
m[1, :]

# 19: 2x2 sub-matrix (e.g. top-left)
m[0:2, 0:2]

# 20: reverse
a[::-1]

# 21: replace 3rd element with 99
a[2] = 99

# 22: >10
a[a > 10]

# 23: even to 0
a[a % 2 == 0] = 0

# 24: divisible by 3
a[a % 3 == 0]

# 25: count > mean
mean_val = a.mean()
count = (a > mean_val).sum()

# Level 4: Shape & broadcasting (36–45)
# Concepts:

# reshape, flatten, ravel, transpose

# np.vstack, np.hstack

# Broadcasting for vector + matrix

# Multiply per column/row using broadcasting

# reshape or reshape(-1, ...) to reduce dimensions

# Shape comparison via .shape
# 36: reshape
a = np.arange(12)
m = a.reshape(3, 4)

# 37: flatten
flat = m.flatten()

# 38: transpose
mt = m.T

# 39: vertical stack
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
v = np.vstack((a1, a2))

# 40: horizontal stack
h = np.hstack((a1, a2))

# 41: broadcasting add [1,2,3]
M = np.array([[10, 20, 30],
              [40, 50, 60]])
v = np.array([1, 2, 3])
res = M + v

# 42: subtract mean from every element
mean_val = a.mean()
centered = a - mean_val

# 43: multiply each column by vector
M = np.array([[1, 2, 3],
              [4, 5, 6]])
col_factors = np.array([1, 10, 100])   # shape (3,)
M_scaled = M * col_factors   # broadcast across rows

# 44: 3D to 2D
x = np.random.rand(2, 3, 4)   # e.g.
x2d = x.reshape(2, -1)        # or (-1, 4) depending on need

# 45: same shape?
B = np.random.rand(2, 3, 4)   
A = np.random.rand(2, 3, 4)   
A.shape == B.shape

