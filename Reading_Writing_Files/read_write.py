import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("some text\nMore text\nAdn even more text")

with open("mydata.txt", encoding="utf-8") as myFile:
    print(myFile.read())