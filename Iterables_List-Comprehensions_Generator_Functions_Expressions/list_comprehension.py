print([2 * x for x in range(1, 11)])

print([x for x in range(1, 11) if x % 2 != 0])

print([i ** 2 for i in range(1, 51) if i % 8 == 0])

print([x * y for x in range(1, 3) for y in range(11, 16)])

# Generate list of 10 values
# Multiply by 2
# Return multiples of 8
print([x for x in [i * 2 for i in range(10)] if x % 8 == 0])