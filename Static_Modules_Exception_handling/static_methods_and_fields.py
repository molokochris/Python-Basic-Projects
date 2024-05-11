# Static methods
'''
class Sum:

    @staticmethod
    def getSum(*args):

        sum = 0

        for i in args:
            sum += i

        return sum

def main():
    print("Sum = ", Sum.getSum(1, 2, 3, 4, 5))

main()
'''
# static variable/Fields
class Dog:

    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name

        Dog.num_of_dogs  += 1

    @staticmethod
    def getNumDogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))

def main():

    spot = Dog("Spot")

    steve = Dog("steve")

    spot.getNumDogs()
    steve.getNumDogs()



main()