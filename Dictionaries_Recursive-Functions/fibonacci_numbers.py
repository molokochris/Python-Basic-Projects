def fib(fn):
    if (fn == 0):
        return 0
    elif (fn == 1):
        return 1
    else:
        fn = fib(fn -1) + fib(fn - 2)
        return fn



def main():
    userInput = int(input("How many numbers do you want to print: "))
    
    for i in range(1, userInput + 1):
        print(fib(i), end=", ")
    print()

main()