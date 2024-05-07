import random
import math

def gen_list():
    rand_list = []
    for i in range(5):
        rand_list.append(random.randrange(1,9))

    return rand_list

def sort_list(list):
    for index in range(len(list) - 1, 0, -1):
        i = 0
        while (i < index):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
            i += 1
    return list

def main():
    rand_list = gen_list()
    print("random list: ", rand_list)
    sorted_list = sort_list(rand_list)
    print("sorted list: ", sorted_list)

main()