# Goal:
# Enter Curstomer (Yes/No) : y
# Enter Curstomer Name : Moloko Poopedi
# Enter Curstomer (Yes/No) : y
# Enter Curstomer Name : Silk Smith
# Enter Curstomer (Yes/No) : n
# Moloko Poopedi
# Silk Smith

customerDict = []

while True:
    try:
        addCustomer = input("Enter Customer (Y/N): ")
        if (addCustomer.lower() == "y"):
            lName, fName = input("Enter Customer Name: ").split()
            customerDict.append({"lName":lName, "fName":fName})
        elif (addCustomer.lower() == "n"):
            for item in customerDict:
                print(item["lName"], item["fName"])
            break
        else:
            print("You've entered a wrong character!")
    except:
        print("something went wrong, try again..")