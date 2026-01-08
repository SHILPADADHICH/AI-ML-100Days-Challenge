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
