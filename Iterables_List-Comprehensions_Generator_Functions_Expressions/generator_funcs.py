def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def genPrime(max_num):
    for num1 in range(2, max_num):
        if isPrime(num1):
            yield num1
        
prime = genPrime(50)

print("Prime:", next(prime))
print("Prime:", next(prime))
print("Prime:", next(prime))
print("Prime:", next(prime))
print("Prime:", next(prime))
