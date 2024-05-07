import math

# Generating a multiplication table
# Example:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 
# 2, 4, 6, 8, 10, 12, 14, 16, 18, 
# 3, 6, 9, 12, 15, 18, 21, 24, 27, 
# 4, 8, 12, 16, 20, 24, 28, 32, 36, 
# 5, 10, 15, 20, 25, 30, 35, 40, 45, 
# 6, 12, 18, 24, 30, 36, 42, 48, 54, 
# 7, 14, 21, 28, 35, 42, 49, 56, 63, 
# 8, 16, 24, 32, 40, 48, 56, 64, 72, 
# 9, 18, 27, 36, 45, 54, 63, 72, 81, 

# Solution 1:
for i in range(1,10):
    for j in range(1,10):
        print(i * j, end=", ")
    print()

# solution 2:
# numList = [i * 1 for i in range(1,10)]
# listOfValues = [[j * i for i in range(1,10)] for j in numList]
# for i in listOfValues:
#     print(i)