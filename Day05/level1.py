import numpy as np

# 1: 1..10


arr = np.arange(1, 11)

# 2: zeros (3,3)
z = np.zeros((3, 3))

# 3: full of 7, 3x4
f = np.full((3, 4), 7)

# 4: identity 5x5
I = np.eye(5)

# 5: 10 evenly spaced between 0 and 1
lin = np.linspace(0, 1, 10)

# 6: props
a = np.array([5, 10, 15, 20, 25])
a.shape, a.size, a.dtype

# 7: list to array
a = np.array([1, 2, 3, 4])

# 8: arange with step 2
ar = np.arange(0, 21, 2)

# 9: random (2,3) between 0 and 1
r = np.random.rand(2, 3)

# 10: random ints
ri = np.random.randint(1, 101, size=(4, 4))

# 11: .ndim for 3D
x = np.zeros((2, 3, 4))
x.ndim   # 3

# 12: int to float
a = np.array([1, 2, 3])
a_float = a.astype(float)

# 13: boolean array from [1, 0, 3, 0]
b = np.array([1, 0, 3, 0], dtype=bool)

# 14: total in (5,6)
np.zeros((5, 6)).size   # or 5*6

# 15: empty (uninitialized content)
e = np.empty((3, 3))
