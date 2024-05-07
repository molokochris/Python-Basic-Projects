import os

with open("mydata.txt", encoding="utf-8") as myFile:
    # Solution 1:
    # for line in myFile:
    #     wordNum = len(line.split())
    #     lttrNum = 0
    #     for lttr in line:
    #         if lttr != " ":
    #             lttrNum += 1
        
    #     print(wordNum, " words : ", lttrNum, " letters: ", lttrNum/wordNum, " avg letters per word")

    # Solution 2:
    lineNum = 1

    while True:
        line = myFile.readline()

        if not line:
            break
        
        print("Line", lineNum)
        # split()
        wordList = line.split()

        print("Number of words: ", len(wordList))

        charCount = 0

        for word in wordList:
            for char in word:
                charCount += 1

        avgNumChars = charCount/len(wordList)

        print("Avg word Length: {:.2}".format(avgNumChars))

        lineNum += 1