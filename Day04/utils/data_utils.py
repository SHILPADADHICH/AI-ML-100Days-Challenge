def average(nums):
    return sum(nums)/len(nums)

def count_missing(data):
    for item in data:
        if item is None:
            return True
    return False
