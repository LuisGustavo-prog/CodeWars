# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.

def sum_mix(arr):
    return sum(list(int(x) for x in arr))

print(sum_mix(arr=[9, 3, '7', '3']))
