
# DAY03 

🔁 Control Flow

Make your programs smart by letting them make decisions

Control flow allows your program to decide what to do based on conditions and to repeat actions when needed. This is the foundation of logic building in programming.

🔹 If Statements

Teach your code how to decide

What are if statements?

if statements allow your program to check a condition and act based on whether it’s True or False.

Real-life logic examples:

IF it’s raining → take an umbrella

IF battery < 20% → charge the phone

IF password is correct → allow access

Basic if statement
age = 18

if age >= 18:
    print("You can vote!")
    print("You're an adult")

How it works:

Python checks the condition age >= 18

If it’s True, the indented code runs

If it’s False, Python skips the block

📌 Important:

The colon : is mandatory

Indentation defines what belongs inside the if block

🔹 If–Else Statements

Handle both possible outcomes

temperature = 25

if temperature > 30:
    print("It's hot!")
else:
    print("Nice weather!")


If the if condition fails, the else block automatically runs.

🔹 If–Elif–Else Chains

Check multiple conditions

score = 85

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")

Key points:

Python checks conditions top to bottom

The first True condition runs

Remaining conditions are skipped

💡 Why use elif instead of multiple if statements?
Because elif stops checking once a condition is met, making your code efficient and correct.
👉 Always place more specific conditions first.

🔹 Multiple Conditions

Combine logic using operators

age = 25
has_license = True

# Both must be True
if age >= 18 and has_license:
    print("You can drive!")

# At least one must be True
if weekend or holiday:
    print("No work today!")

# Reverse a condition
if not raining:
    print("Let's go outside!")

🔹 Nested If Statements

If inside another if

has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Need adult supervision")
else:
    print("Buy a ticket first")

❌ Common Mistakes (If Statements)

Forgetting the colon :

Using = instead of ==

Incorrect indentation

🔁 Loops

Repeat actions without rewriting code

What are loops?

Loops allow you to execute the same block of code multiple times automatically.

Without loops:
print("Hello!")
print("Hello!")
print("Hello!")
print("Hello!")
print("Hello!")

With loops:
for i in range(5):
    print("Hello!")


✔ Same result, cleaner code!

🔹 For Loops

Most commonly used loop in Python

Repeat a fixed number of times
for i in range(5):
    print(i)


📌 Output:

0
1
2
3
4


Python uses zero-indexing, so range(5) gives numbers from 0 to 4.

Custom ranges
# Count from 1 to 5
for i in range(1, 6):
    print(i)

# Count by 2s
for i in range(0, 10, 2):
    print(i)

🔹 Loop Through Text
name = "Python"

for letter in name:
    print(letter)

🔹 Loop Through a List (Preview)
colors = ["red", "blue", "green"]

for color in colors:
    print(f"I like {color}")

🔹 While Loops

Run while a condition stays True

count = 0

while count < 5:
    print(f"Count is {count}")
    count = count + 1


⚠️ Always update the variable inside a while loop, or it will run forever!

❌ Common Loop Mistakes

Missing colon :

Wrong indentation

Off-by-one errors

🔀 Loop Control Statements
🔹 break — Stop loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)

🔹 continue — Skip current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)

⚡ Comprehensions (Very Important ⭐)

Short and powerful way to write loops

🧠 List Comprehension
squares = [i*i for i in range(5)]
print(squares)

With condition:
even = [i for i in range(10) if i % 2 == 0]

🧠 Dictionary Comprehension

A concise way to create dictionaries using a loop.

square_dict = {i: i*i for i in range(5)}

🚀 Early AI/ML Exposure

Dictionary comprehension → feature mapping, label encoding

Set comprehension → removing duplicate data points

🕒 Coding Practice (2.5 Hours): 40 Challenges
🔹 Beginner (15)

Even or odd check

Largest of 3 numbers

Sum of first N numbers

Multiplication table

Digit count

🔹 Intermediate (15)

Fibonacci series

Prime number check

Reverse a number

Palindrome check

Count vowels

Factorial using loop

🔹 Advanced (10)

Pattern printing

Armstrong number

Number guessing logic

List comprehension problems

Frequency counting

🟢 CodeChef Practice Links

(For real competitive exposure)

🔰 Beginner

https://www.codech
ef.com/problems/FLOW006

https://www.codechef.com/problems/INTEST

https://www.codechef.com/problems/FLOW008
⚡ Loops & Conditions

https://www.codechef.com/problems/FSQRT

https://www.codechef.com/problems/START01

https://www.codechef.com/problems/FLOW004

🔥 Logic Building

https://www.codechef.com/problems/HS08TEST

https://www.codechef.com/problems/LUCKYFOUR

🎯 Target: Solve 8–10 CodeChef problems, not all 40.
The rest should be solved through self-practice and experimentation.