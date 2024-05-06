import math

def get_area(shape):
    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "square":
        square_area()
    elif shape == "triangle":
        triangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("shape entered does not exist, please enter triangle, square, circle or rectangle")

def rectangle_area():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))

    area = length * width
    print(f"Area of the rectangle is {area}")

def square_area():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))

    area = length * width
    print(f"Area of the square is {area}")
def triangle_area():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    height = float(input("Enter the height: "))

    area = length * width * height
    print(f"Area of the triangle is {area}")
def circle_area():
    radius = float(input("Enter the radius: "))

    area = math.pi * (math.pow(radius, 2))
    print("Area of the circle is {:.2f}".format(area))

def main():
    shape_type = input("name of shape: ")

    get_area(shape_type)

main()