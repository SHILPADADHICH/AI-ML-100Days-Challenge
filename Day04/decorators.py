# 🧠 Decorator Question 1: Execution Time Tracker (MUST-DO)
# 🎯 Problem Statement

# Create a decorator called time_tracker that:

# Measures how long a function takes to execute

# Prints the execution time in seconds

# Works for any function (no arguments, for now)

import time
def time_tracker(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        execution_duration = end_time - start_time
        print(f"Execution time: {execution_duration} seconds")
    return wrapper
@time_tracker
def sample_func():
    total = 0.1
    for i in range(1,100):
        total *= i
    print("Sample function executed.",total)
sample_func()


# 🧠 Decorator Question 2: Login Required Decorator (REAL-WORLD LOGIC)
# 🎯 Problem Statement

# Create a decorator called login_required that:

# Checks if a user is logged in

# If logged in → run the function

# If not → print "Please login first"

def Login_required(func):
    def wrapper(is_logged_in):
        if is_logged_in:
            func()
        else:
            print("Please login first")
    return wrapper


def sample_fucntion():
    print("Function executed successfully.")
Login_required(sample_fucntion)(False)  # Should print "Please login first"
Login_required(sample_fucntion)(True)   # Should execute the function
