'''
    ------------ PROBLEM ----------
    1. Create regular expression that prints each line in the string
    2. Print out the number of matches
    3. Output result
'''
import re

randStr = '''Just some words
and some more\r
and more
'''

regex = re.compile("[^\n]+[\r]*")
matches = re.findall(regex, randStr)

# for match in matches:
#     print(match)

print(matches)
