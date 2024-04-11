# Problem: have the user enter the investment amount and expected interest
#   Each year the investment will increase by 
#       original investment + their investment * interest rate is
# Solution:
# Ask for money investment + interest rate
investment, iRate = input("Enter investment amount and interest rate: ").split()

# convert the value to float
investment = float(investment)

# convert value to float and round percentage rate by 2 digits
iRate = float(iRate) * .01

# cycle through 10 years using for loop and range
for i in range(10):
    investment = investment + (investment * iRate)

# output the results
print("Total accumulated is {:.2f} ".format(investment))
