from utils import square, cube, is_even 
from utils import average, count_missing

num = 2
print(f"Square of {num} is {square(num)}")
print(f"Cube of {num} is {cube(num)}")

nums = [1, 2, 3, 4, 5]
print(f"Average of {nums} is {average(nums)}")
print(f"Is {num} even? {'Yes' if is_even(num) else 'No'}")

data = [1, 2, None, 4]
print(f"Does data {data} have missing values? {'Yes' if count_missing(data ) else 'No'}")


