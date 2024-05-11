'''
    ---------- PROBLEM ----------
    Create a random list filled with the characters H and T
    for heads and tails. Output the number of Hs and Ts
    Example Output
    Heads : 46
    Tails : 54
'''

import random

coinFlips = [random.choice(("H", "T")) for i in range(100)]

print(f"Heads:{coinFlips.count('H')}\n\
Tails:{coinFlips.count('T')}")