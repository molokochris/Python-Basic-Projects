# 1. Create a file name mydata2.txt
# 2. open a file without using with (Open in try)
# 3. Catch FileNotFoundError
# 4. In else print contents
# 5. In Finally
# 6. Open nonexistent file mydata3.txt

import os

try:
    # a: append, w: write(overrideds existing data, r: read)
    f = open("mydata2.txt", "w")
    f.write("This is the text you want to see\nthis is even more text on a new line")
    f.close()

except FileNotFoundError as F404:
    print("File: {} does not exist..\n{}".format(f.name, F404.args))

else:
    f = open("mydata2.txt", "r")
    print("File: ", f.read())
    f.close()

finally:
    f = open("mydata3.txt", encoding="utf-8")
    print(f.read())
    f.close()