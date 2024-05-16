import re

randStr = "doctor doctors doctor's"

# ? - includes 0 or 1 character that proceeeds the match (makes it include both cat & cats)
regex = re.compile("[doctor]+['s]*?")

matches = re.findall(regex, randStr)

for match in matches:
    print(match)