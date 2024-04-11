# Ask the user to input 2 values ad store them in variables num1 an num2
num1, num2 = input('Ennter 2 numbers: ').split()

# convert the strings user enters to numbers Intergers
num1 = int(num1)
num2 = int(num2)

# Add the values and store into variable named sum
sum = num1 + num2

# subtract values and store in variable named difference
difference = num1 - num2

# multiply and store in product
product = num1 * num2

# Divide and store in quotient
quotient = num1 / num2

# use modulus and store in remainder
remainder = num1 % num2

# print the results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
