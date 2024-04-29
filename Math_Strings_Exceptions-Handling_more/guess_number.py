import random

# this is a guessing game
# user guesses the number our random generator has saved
# if correct, we print "you've guessed it right"
# else, it continues asking

rand_num = random.randrange(1, 11)

while True:
    try:
        number = int(input("Please guess a number between 1 and 10: "))
        print("random number: ", rand_num)
        # break
        if (number == rand_num):
            print("you've guessed it right!!!")
            break
    except ValueError:
        print("You didnt enter a number")
    except:
        print("An unknown error occurred.")
