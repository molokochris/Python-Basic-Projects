while True:
    try:
        number = int(input("Please enter any number: "))
        break
    
    except ValueError:
        print("You did not enter a number")

    except:
        print("An unknown error occured")
print("Thank you for entering a number")