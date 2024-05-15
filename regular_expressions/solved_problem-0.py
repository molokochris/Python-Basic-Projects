import re

'''
    -------------------- PROBLEM --------------------
    Create a regular expression that will match email addresses from
    a list
    RULES:
    1. 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
    2. An @ symbol
    3. 2 to 20 lowercase and uppercase letters, numbers, plus .-
    4. A period
    5. 2 to 3 lowercase and uppercase letters
'''

emailList = ["molokochrisp742@gmail.com","mcpooedi@gmail.c1m", "w1ll8-po%+_@outlo-k..com"]

for mail in emailList:
    if (re.search("[\w._%+-]{1,20}@[\w.-]{2,20}\\.[A-Za-z]{2,3}", mail)):
        print("{} - is a valid email".format(mail))
    else:
        print("{} - is not a valid email".format(mail))

# SOLUTION 02:

# counts the number of valid email addresses using findall(accepts strings as arguments)
# after join the list items with a whitespace(turning list to string)
print("Email matches:", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}\\.[A-Za-z]{2,3}", " ".join(emailList))))
