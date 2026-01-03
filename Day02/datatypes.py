total = 5 + 5
print(total)
# Numbers can do math
total = 10 + 5  # 15

# Strings combine differently  
name = "Hello" + "World"  # "HelloWorld"

# Can't mix without converting
# age = "25" + 5  # Error!
age = int("25") + 5  # 30 (converted string to number)

# Check different types
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("Hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>
print(type(5 + 3))

# Check variables
age = 25
name = "Alice"
print(type(age))         # <class 'int'>
print(type(name))        # <class 'str'>

#float vs integer division
# Regular division (always float)
result = 10 / 3    # 3.333...

# Integer division (rounds down)
result = 10 // 3   # 3

#Can't use commas in numbers

# Wrong
million = 1,000,000  # Creates a tuple, not a number!

# Right
#can't use commas in numbers
million = 1000000    # Hard to read
million = 1_000_000  # Python style

#Strings:
name = "Shilpa"
greet = 'Hello Guys'

# Single quotes
first = 'Python'

# Double quotes  
second = "Python"

# Triple quotes for multiple lines
paragraph = """This is
a multi-line
string"""

#Use double quotes when your text contains apostrophes: "It's Python!"

#String Operations

#Contactenation
first_name = "Shilpa"
last_name = "Dadhich"

full_name = first_name + " " + last_name 
print(full_name)

#Repetition
laugh = "He" *5
print(laugh)  # HeHeHeHeHe


#String length
length = len(full_name)
print(length)  # 13

#Converting to String

age = 21
message = "I am "+str(age)+" years old."
print(message)

# Or use f-strings (we'll learn more later)
message = f"I am {age} years old"

#Boolean Data Type

is_student = True
has_graduated = False
#Boolean values are True and False with capital letters. Using true or false will cause an error!

age = 20
is_adult = age>18
print(is_adult)  # True

#operators: and, or, not

#Logical Operators
age = 25
has_license = True

# AND - both must be true
can_drive = age >= 16 and has_license
print(can_drive)  # True

# OR - at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)  # True

# NOT - reverses the value
is_adult = age >= 18
is_child = not is_adult
print(is_child)  # False

#String Methods

text = "Python Programming"

print(text.lower())      # "python programming"
print(text.upper())      # "PYTHON PROGRAMMING"
print(text.title())      # "Python Programming"

messy = "  hello world  "
print(messy.strip())     # "hello world" (removes whitespace)

price = "$19.99"
print(price.strip("$"))  # "19.99"

message = "I love Python programming with Python"

# Check if something exists
print("Python" in message)        # True
print(message.startswith("I"))   # True
print(message.endswith("Python")) # True

# Find position
print(message.find("Python"))     # 7 (first occurrence)
print(message.count("Python"))    # 2 (number of times)

# Replace
new_message = message.replace("Python", "JavaScript")
print(new_message)  # "I love JavaScript programming with JavaScript"

# Wrong - mismatched quotes
#text = 'It's Python'

# Right - escape or use different quotes
text = "It's Python"  # Double quotes outside
text = 'It\'s Python'  # Escape the apostrophe