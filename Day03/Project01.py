#Simple Calculator

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Choose an operation: ")

for i in ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Division"]:
    print(i)
operation = input("Enter operation (1/2/3/4): ")

if operation == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif operation == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif operation == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))       
elif operation == '4':
    print(num1, "/", num2, "=", divide(num1, num2)) 
