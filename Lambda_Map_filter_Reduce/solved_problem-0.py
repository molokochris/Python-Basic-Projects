'''
    ---------- PROBLEM ----------
    Create a function that receives a list and a function
    The function passed will return True or False if a list
    value is odd
    The surrounding function will return a list of odd
    numbers
'''

def oddNumList(list, func):
    oddList = []
    
    for i in list:
        if func(i):
            oddList.append(i)

    return oddList

# def isListOdd(value):
    
#     if (value % 2) > 0:
#         return True
        
    
#     return False

# sumList = [2, 4, 6, 8, 10, 11, 13, 3, 14, 18, 19]

# print(oddNumList(sumList, isListOdd))