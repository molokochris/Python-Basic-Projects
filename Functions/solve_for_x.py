# a simple solveForX function that
# receives a string that contains a math problem to be solved
# - we will onnly deal with addition expressions

math_problem = input("enter your expression: ")


def solveForX(equation):
    global math_problem
    x, operator, num1, equal, num2 = equation.split()

    num1, num2 = int(num1), int(num2)
    return (str(x) + " = " + str(num2 - num1))

print(solveForX(math_problem))
print("math_problem: ", math_problem)