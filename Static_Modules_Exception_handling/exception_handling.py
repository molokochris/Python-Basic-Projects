# try:
#     aList = [1,2,3]

#     print(aList[3])

# # except(IndexError, NameError)

# except IndexError:
#     print("Looks like you're printing a invalid index")

# except:
#     print("something occured, try again.")

''' this example inherit from the python exception class: '''

# class DogNameError(Exception):

#     def __init__(self,*args, **kwargs):
#         # **kwargs : key word arguments
#         Exception.__init__(self, *args, **kwargs)

# try:
#     dogName = input("What is your dog name: ")
    
#     if any(char.isdigit() for char in dogName):
#         raise NameError

# except DogNameError:
#     print("Dog name cannot contain number..") 

''' raising custom exception '''

class DogNameError(Exception):

    def __init__(self,*args, **kwargs):
        # **kwargs : key word arguments
        Exception.__init__(self, *args, **kwargs)

try:
    dogName = input("What is your dog name: ")
    
    if any(char.isdigit() for char in dogName):
        raise DogNameError

except DogNameError:
    print("Dog name cannot contain number..") 