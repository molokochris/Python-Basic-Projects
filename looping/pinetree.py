rows = input("How tall is the treee!? ")

rows = int(rows)
treeRow = 1

for i in range(rows):
    spaces = i
    if (spaces < (rows)):
        while ((rows - spaces) > 0):
            print(" ", end="")
            spaces += 1

    for i in range(treeRow):
        print("#", end="")
    treeRow += 2
    print("")
for i in range(rows):
    print(" ", end="")
print("#")