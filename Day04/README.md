### 🔹 1. Functions (The Heart of Python)
What is a Function?

A function is a reusable block of code that performs a specific task.

Instead of writing the same logic again and again, you write once, use many times.

Real-life analogy

Think of a mixer:

You give ingredients (inputs)

Press a button

You get paste (output)

Same with functions.

Basic Function Syntax
```python
def function_name(parameters):
    # code
    return result

```
Example
```python
def add(a, b):
    return a + b

print(add(3, 5))  # 8

```
Why use functions?

✅ Clean code
✅ Avoid repetition
✅ Easy debugging
✅ Required in ML pipelines

Types of Functions (Important)
1️⃣ Function with parameters & return value
```python
def square(x):
    return x * x

```
Used in ML for:

Feature transformation

Scaling

Mathematical operations

2️⃣ Function without return
```python
def greet():
    print("Hello AI Learner!")

```
Used for:

Logging

Printing progress

3️⃣ Default parameters
```python
def power(base, exp=2):
    return base ** exp

```
power(3)     # 9
power(3, 3)  # 27

Used when:

You want flexibility

Common defaults in ML (epochs=10, lr=0.01)

4️⃣ Keyword arguments
```python
def student(name, age):
    print(name, age)

```
student(age=20, name="Shilpa")

Used in:

Model configs

APIs

Why Functions Matter in AI/ML?

Data cleaning → function

Feature engineering → function

Model training → function

Evaluation → function

```python
### 💡 Every ML project = functions talking to each other

```
### 🔹 2. Decorators (Power Feature 🚀)

Decorators look scary but are very logical.

What is a Decorator?

A decorator is a function that adds extra behavior to another function without changing its code.

Real-life analogy

You have a gift 🎁
You add:

Wrapping paper

Ribbon

The gift stays same, presentation improves.

Function inside a Function (Foundation)
```python
def outer():
    def inner():
        print("Inside inner")
```
inner()

outer()

Python allows functions inside functions.

Functions as Arguments
```python
def shout(text):
    return text.upper()

def speak(func):
    print(func("hello"))

```
speak(shout)

➡️ Functions are objects in Python.

Basic Decorator Example
Step 1: Normal function
```python
def greet():
    print("Hello!")

```
Step 2: Decorator
```python
def my_decorator(func):
    def wrapper():
        print("Before function")
```
func()
```python
        print("After function")
    return wrapper

```
Step 3: Apply decorator
@my_decorator
```python
def greet():
    print("Hello!")

```
greet()

Output
Before function
Hello!
After function

Why Decorators are Used?

✅ Logging
✅ Timing functions
✅ Authentication
✅ Validation
✅ Caching

Real ML Use Case – Time a function
```python
import time

def timer(func):
    def wrapper():
        start = time.time()
```
func()
```python
        end = time.time()
        print("Time:", end - start)
    return wrapper

```
@timer
```python
def train_model():
    for i in range(1000000):
```
pass

train_model()

Used in:

Measuring training time

Optimization

### 🔹 3. Imports & Libraries
What is a Library?

A library is a collection of pre-written code.

You don’t build everything from scratch.

Example libraries

math → math functions

random → randomness

numpy → numerical computing

pandas → data analysis

matplotlib → visualization

Importing Libraries
1️⃣ Import whole library
```python
import math
```
math.sqrt(16)

2️⃣ Import specific functions
```python
from math import sqrt
```
sqrt(16)

3️⃣ Alias (VERY common)
```python
import numpy as np

```
Used everywhere in ML.

Why Libraries Matter in AI/ML?

Without libraries:

You’d manually code matrix multiplication 😵

Training models would take years

Libraries give:
### ⚡ Speed
### ⚡ Accuracy
### ⚡ Reliability

### 🔹 4. Build 5 Utility Functions (Coding Task)

Examples you should build 👇

1️⃣ Mean of list
```python
def mean(nums):
    return sum(nums) / len(nums)

```
2️⃣ Normalize data
```python
def normalize(nums):
    max_val = max(nums)
    return [x / max_val for x in nums]

```
3️⃣ Count missing values
```python
def count_none(data):
    return data.count(None)

```
4️⃣ Check prime
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

```
5️⃣ Accuracy calculator
```python
def accuracy(y_true, y_pred):
    correct = 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
```
correct += 1
```python
    return correct / len(y_true)

```
### 🔹 5. Personal Utility Library (Lab Task)
Folder Structure
utils/
├── __init__.py
├── math_utils.py
├── data_utils.py

math_utils.py
```python
def square(x):
    return x * x

```
data_utils.py
```python
def mean(nums):
    return sum(nums) / len(nums)

```
Using it
```python
from utils.math_utils import square
print(square(5))

```
### 🧠 Day 4 Takeaway

```python
Functions = building blocks

Decorators = power-ups

Libraries = productivity boost

Utility library = professional habit
```