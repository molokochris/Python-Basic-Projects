# sum = lambda x, y: x + y

# print("Sum: ", sum(4, 5))

# can_vote = lambda age: True if age >= 18 else False

# print("Can Vote: ", can_vote(27))

# powerList = [lambda x: x ** 2, 
#              lambda x: x ** 3,
#              lambda x: x ** 4,]

# for func in powerList:
#     print(func(4))

attack = {'quick': (lambda: print("Quick attack")),
          'power': (lambda: print("Power attack")),
          'miss': (lambda: print("Missed attack"))}

attack['quick']()

import random

attackKey = random.choice(list(attack.keys()))

attack[attackKey]()