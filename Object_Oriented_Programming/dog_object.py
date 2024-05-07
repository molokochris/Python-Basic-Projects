class Dog:

    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

    def barks(self):
        print("{} the dogs barks".format(self.name))
    
    def eats(self):
        print("{} the dogs eats".format(self.name))

    def sleeps(self):
        print("{} the dogs sleeps".format(self.name))

def main():
    spot = Dog("spot", 66, 42)

    spot.barks()
    spot.eats()

main()