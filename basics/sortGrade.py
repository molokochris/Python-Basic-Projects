# if age is 5, go to kindergarten
age = eval(input("enter age "))

if (age == 5):
    print("Go to kindergarten")
# age 6 - 17, grade 1 -> 12
elif (age >= 6) and (age <= 17):
    print("Go to grade {}".format(age - 5))
# if age > 17, go to college
elif (age > 17):
    print("Go to College")
else:
    print("stay at home")
# try to complete with 10 or less lines
