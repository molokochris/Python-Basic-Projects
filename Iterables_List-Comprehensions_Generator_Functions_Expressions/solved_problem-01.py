'''
    ---------- PROBLEM ----------
    Generate a list of 50 random values between 1 and 1000
    and return those that are multiples of 9
    You'll have to use a list comprehension in a list comprehension
'''
import random

randList = [i for i in [random.randrange(1, 1001) for i in range(50)] if i % 9 == 0]
print(randList)