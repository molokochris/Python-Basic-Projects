# Regular expressions also (regex)
import re

# if re.search("ape", "the ape was at the apex"):
#     print("there is an ape")

# allApes = re.findall("ape", "the ape was at the apex")

# for i in allApes:
#     print(i)

# print("-->")

# allApes = re.findall("ape.", "the ape was at the apex")

# for i in allApes:
#     print(i)

# theStr = "The ape was at the apex"

# for i in re.finditer("ape.", theStr):

#     locTuple = i.span()

#     print(locTuple)

#     print(theStr[locTuple[0]:locTuple[1]])

# animalStr = "Cat rat mat pat"

# # allAminals = re.findall("[crmfp]", animalStr)

# # for i in allAminals:
# #     print(i)

# someAnimals = re.findall("[c-mC-M]at", animalStr)
# for i in someAnimals:
#     print(i)

# print()
# # excludes words that start with (C/r)
# someAnimals = re.findall("[^Cr]at", animalStr)
# for i in someAnimals:
#     print(i)

# owlFood = animalStr

# regex = re.compile("[Cr]at")

# owlFood = regex.sub("owl", owlFood)

# print(owlFood)

# randStr = "Here is \\stuff"

# print("Find \\\\stuff: ", re.search("\\\\stuff", randStr))
# # solution 2: (row string(r))
# print(r"Find \\stuff: ", re.search(r"\\stuff", randStr))

# randStr = "F.B.I. I.R.S. CIA"

# print("Matches: ", len(re.findall(".\..\..\.", randStr)))

# ------------------------------>

##\b : backspace
##\f : form feed
##\r : carriage return
##\t : tab
##\v : vertical tab

#randStr = '''This is a long
#string that goes
#on for many lines
#'''
#print(randStr)

#regex = re.compile("\n")

#randStr = regex.sub(" ", randStr)

#print(randStr)

#-------------------------------------------------->

# \d: [0-9]
# \D: [^0-9]

randStr = "12345"

print("Matches: ", len(re.findall("\d", randStr)))
# specifically searches for 5 numbers
print("Matches: ", len(re.findall("\d{5}", randStr)))
