# Enter Calculation: 5 * 6
# Output: 5 * 6 = 30

# Store input inside 3 variables num1, operator, num2
num1, operator, num2 = input("Enter Calculation: ").split()

# convert strings to integers
num1 = int(num1)
num2 = int(num2)

# perform calculations
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    result = num1 % num2

# print the results
print("{} {} {} = {}".format(num1, operator, num2, result))
