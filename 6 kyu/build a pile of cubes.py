# Your task is to build a building that will be a stack of n cubes. The cube at the bottom will have a volume of n³, the cube above it will have a volume of (n-1)³, and so on, until the top cube which will have a volume of 1³.

# You are given the total volume m of the building. Given m, you need to find the number n of cubes you must build.

# The function will receive an integer m, and you must return the integer n such that:

# n³ + (n-1)³ + (n-2)³ + ... + 1³ = m

# If such an n does not exist, return -1.

def find_nb(m):
    n, result_m = 1, 1

    while result_m < m:
        n += 1
        
        result_m += n ** 3

    return n if result_m <= m else -1

# def find_nb(m):
#     i,sum = 1,1
#     while sum < m:
#         i+=1
#         sum+=i**3
#     return i if m==sum else -1


print(find_nb(9))

# print(find_nb(24723578342962))
