max_range = int(input("Enter max prime range: "))

def is_prime(num):
    if not(num % 2 == 0):
        return num

def prime_list(max):
    prime_nums = []
    for i in range(max + 1):
        if is_prime(i):
            prime_nums.append(i)
    return prime_nums

print(prime_list(max_range))