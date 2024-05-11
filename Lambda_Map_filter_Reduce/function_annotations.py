
def random_funct(name: str, age: int, weight: float) -> str:
    print("Name: ", name)
    print("Age: ", age)
    print("Weight: ", weight)

    return "{} is {} years old and weighs {}".format(name, age, weight)

print(random_funct("Chris", 27, 78.9))
print(random_funct(12, "Chris", "Poopedi"))
print(random_funct.__annotations__)
