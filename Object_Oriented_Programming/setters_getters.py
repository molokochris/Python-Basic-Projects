class Square:

    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retrieving height..")

        return self.__height
    
    @height.setter
    def height(self,value):
        if value.isdigit():
            self.__height = value
        else:
            print("please only enter numbers for only height")

    @property
    def width(self):
        print("Retrieving width..")

        return self.__width
    
    @width.setter
    def width(self,value):
        if value.isdigit():
            self.__width = value
        else:
            print("please only enter numbers for only width")

    def getArea(self):
        return int(self.__height) * int(self.__width)


def main():

    aSqaure = Square()

    height = input("Height: ")
    width = input("Width: ")

    aSqaure.height = height
    aSqaure.width = width

    print("Height: ", aSqaure.height)
    print("Width: ", aSqaure.width)
    print("Area: ", aSqaure.getArea())


main()