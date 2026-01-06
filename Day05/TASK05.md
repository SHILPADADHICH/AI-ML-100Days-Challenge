# Day 04 | NumPy Introduction 🧮🚀

## 100 Days of AI/ML Challenge

Day 5 is focused on **NumPy**, the backbone of numerical computing in Python and a core requirement for **Data Science, Machine Learning, and Deep Learning**.

---

## 📌 Today's Learning Objectives

By the end of Day 5, I should be able to:

* Understand what NumPy is and why it is used
* Create and manipulate NumPy arrays
* Perform vectorized mathematical operations
* Apply slicing, indexing, and boolean masking
* Understand broadcasting and shape manipulation
* Compare NumPy operations with native Python

---

## ⏰ Time Breakdown

* **Lecture (1.5h)** → NumPy arrays, operations, broadcasting
* **Coding (2.5h)** → 50+ NumPy practice operations
* **Hands-on (1h)** → Array creation, slicing, math operations
* **Challenge (30 min)** → Replicating NumPy behavior using native Python

---

## 📘 Topics Covered

### 1️⃣ NumPy Basics

* What is NumPy and why it is faster than Python lists
* ndarray vs list
* Installing & importing NumPy

### 2️⃣ Array Creation

* `np.array()`
* `np.zeros()`
* `np.ones()`
* `np.full()`
* `np.eye()`
* `np.arange()`
* `np.linspace()`
* `np.random.rand()`
* `np.random.randint()`

### 3️⃣ Array Properties

* `ndim`
* `shape`
* `size`
* `dtype`

### 4️⃣ Indexing & Slicing

* 1D slicing
* 2D indexing
* Row & column selection
* Boolean indexing

### 5️⃣ Mathematical Operations

* Element-wise operations
* Scalar operations
* Universal functions (`sqrt`, `log`, `exp`, etc.)

### 6️⃣ Aggregations

* `sum`, `mean`, `max`, `min`, `std`
* `axis=0` vs `axis=1`

### 7️⃣ Broadcasting

* Broadcasting rules
* Vector + matrix operations

### 8️⃣ Shape Manipulation

* `reshape()`
* `flatten()`
* `ravel()`
* `transpose()`

### 9️⃣ Copy vs View

* Reference issue
* `copy()` method

---

## 🧪 Practice Questions (50)

### 🟢 Level 1: Basics (1–15)

1. Create a 1D NumPy array containing numbers from 1 to 10.
2. Create a 2D array of shape (3, 3) filled with zeros.
3. Create a 3×4 array filled with the value `7`.
4. Create an identity matrix of size 5×5.
5. Create an array of 10 evenly spaced values between 0 and 1.
6. Create an array `[5, 10, 15, 20, 25]` and print its shape, size, and datatype.
7. Convert a Python list `[1, 2, 3, 4]` into a NumPy array.
8. Create an array using `arange()` from 0 to 20 with step 2.
9. Create a random array of shape (2, 3) with values between 0 and 1.
10. Create a random integer array between 1 and 100 of shape (4, 4).
11. Check the number of dimensions of a 3D array.
12. Change the datatype of an array from int to float.
13. Create a boolean array from `[1, 0, 3, 0]`.
14. Find the total number of elements in a (5, 6) array.
15. Create an empty array of shape (3, 3).

### 🟡 Level 2: Indexing & Slicing (16–25)

16. Extract the first three elements from a 1D array.
17. Get the last column of a 2D array.
18. Extract the second row from a matrix.
19. Slice a 2D array to get a 2×2 sub-matrix.
20. Reverse a NumPy array.
21. Replace the 3rd element of an array with `99`.
22. Select all elements greater than 10 from an array.
23. Change all even numbers in an array to `0`.
24. Use boolean indexing to extract values divisible by 3.
25. Count how many values in an array are greater than the mean.

### 🟠 Level 3: Math & Aggregations (26–35)

26. Add two NumPy arrays element-wise.
27. Multiply an array by a scalar value.
28. Compute the square root of each element in an array.
29. Find the sum of all elements in a matrix.
30. Find the mean of each column in a 2D array.
31. Find the maximum value in each row.
32. Calculate the standard deviation of an array.
33. Normalize an array between 0 and 1.
34. Find the index of the maximum value in an array.
35. Compute the dot product of two vectors.

### 🔵 Level 4: Shape & Broadcasting (36–45)

36. Reshape a 1D array of size 12 into a (3, 4) matrix.
37. Flatten a 2D array into 1D.
38. Transpose a matrix.
39. Stack two arrays vertically.
40. Stack two arrays horizontally.
41. Add a 1D array `[1,2,3]` to a 2D array using broadcasting.
42. Subtract the mean of an array from every element.
43. Multiply each column of a matrix by a vector.
44. Convert a 3D array into 2D.
45. Check if two arrays have the same shape.

### 🔴 Level 5: ML-Style Operations (46–50)

46. Replace all negative values in an array with `0`.
47. Use `np.where()` to label values greater than 50 as `1`, else `0`.
48. Find unique elements and their counts in an array.
49. Sort a NumPy array row-wise.
50. Perform mean normalization: `(x - mean) / std`.

---

## 🧠 Challenge Task

Replicate NumPy operations using **native Python only**:

* Element-wise list addition
* Mean calculation
* Matrix addition using loops

---

## ✅ Day 4 Completion Checklist

* [✅] Completed NumPy lecture
* [✅] Solved at least 40 practice questions
* [✅] Understood broadcasting and axis
* [✅] Completed Python-only challenge
* [✅] Code pushed to GitHub

---

## 📍 Outcome of the Day

✔ Strong NumPy foundation
✔ Ready for Pandas and ML math
✔ Reduced dependency on loops

---

**Day 04 Complete ✅**

📌 *Consistency over intensity. Keep going.* 🚀
