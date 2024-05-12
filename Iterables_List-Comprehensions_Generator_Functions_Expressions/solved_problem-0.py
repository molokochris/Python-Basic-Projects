'''
    ---------- PROBLEM ----------
    Create a class that returns values from the Fibonacci
    sequence each time next is called
    Sample Output
    Fib : 1
    Fib : 2
    Fib : 3
    Fib : 5
'''
class FibNums:

    def __init__(self):
        self.currentVal = 0
        self.index = 2
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.currentVal = (self.index - 1) + (self.index - 2) # Formula not correct
        self.index += 1
        if self.currentVal >= 0:
            return self.currentVal
    
fibNum = FibNums()

for i in range(10):
    print("Fib:", next(fibNum)) # but next() works