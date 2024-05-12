# Iterables: stored sequence of values
# Example 01:
sampStr = iter("Sample")

print("Char :", next(sampStr))
print("Char :", next(sampStr))

# Example 02:
class Alphabet:

    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.index >= len(self.letters) - 1):
            raise StopIteration
        self.index += 1
        return self.letters[self.index]

alpha = Alphabet()

for letter in alpha:
    print(letter, end="")
print()

# Example 03 (not exactly):
moloko = {"fName":"Moloko", "sName":"Poopedi"}

for key in moloko:
    print(key, moloko[key])
