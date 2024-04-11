# provide different output based on age
# 1 - 18 -> imprtant
# 21, 50, > 65 -> important
# All others -> not important

# Receive age and store in age
age = eval(input("enter age: "))

# if age is both greater than or equal to 1 and less than or equal to 18 important
if age >= 1 and age <= 18:
    print("Important Birth")

# if age is either 21 or 50 or greater than 65 important
elif age == 21 or age == 50:
    print("Important Birth")

# we check if age is less than 65 and then convert true to false and vice versa
elif not(age < 65):
    print("Important Birth")

# else not important
else:
    print("Not Important")
