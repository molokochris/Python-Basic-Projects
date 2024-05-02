# e.g Random Access Memory : RAM

abbr_string = str(input("Enter word: "))
acr_string = ""
'''
if (abbr_string[0] >= "a" and abbr_string[0] <= "z"):
    acr_string += abbr_string[0].upper()
for i in range(len(abbr_string)-1):
    if (abbr_string[i] == " "):
        acr_string += abbr_string[i + 1].upper()
'''
# OR

temp_list = abbr_string.split()
for string in temp_list:
    acr_string += string[0].upper()

print("The acronym of '{}' is {}".format(abbr_string, acr_string))