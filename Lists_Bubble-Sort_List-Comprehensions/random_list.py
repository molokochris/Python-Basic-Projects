import random

rand_list = []
index = 0
while (index < 5):
    rand_num = random.randrange(1, 9)
    rand_list.append(rand_num)
    index += 1
print(rand_list)