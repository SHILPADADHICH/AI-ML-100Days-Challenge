#Now i will implement some basic functions in Python whatever we learned in datatypes.py

#Function 1: Add Two Numbers
# this will be the syntax for python functions
num1 = 20
num2 = 40
def add(num1,num2):
    return num1 + num2
result = add(num1,num2)
print("Addition:", result)

#Function 2: Check Even or Odd
num = 14
def is_even(num):
    return num%2==0

print(f"{num} is even: {is_even(num)}")

#Function 3: Find Maximum of Two Numbers
def max(a,b):
    if a>b:
        return a
    else:
        return b
print("Maximum:", max(num1,num2))

#Function 4: Calculate Simple Interest
def  simple_interest(pr,rt,t):
    return (pr*rt*t)/100

print("Simple Interest:", simple_interest(num,num1,num2))

#5 Check if a Number Is Prime
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    
    
print(f"{num} is prime: {is_prime(num)}")
