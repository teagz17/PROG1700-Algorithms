# comments

# import modules here
import random

# variables
invalid_attempts = 3

# program control
while invalid_attempts > 0:
    # local variable user_input
    user_input = input("press 1 for rock, 2 for paper, or 3 for scissors: ")
    # validate the input to ensure the program doesn't have invalid input
    # return true if a digit is entered, otherwise return false
    if user_input.isdigit():
        # cast to an integer
        user_input = int(user_input)
        # custom messages
        if user_input == 1:
            print("you picked rock!")
        if user_input == 2:
            print("you picked paper!")
        if user_input == 3:
            print("you picked scissors!")
        # ensure 1, 2, 3 numbers only
        if user_input <=3 and user_input >=1:
            # calculate and show the computer's value
            computer_value = random.randrange(1,4,1)
            print("computer picked...")
            if computer_value == 1:
                print("rock!")
            if computer_value == 2:
                print("paper!")
            if computer_value == 3:
                print("scissors!")
            # check for tie
            if user_input == computer_value:
                print("it's a tie!")
            # run the game
            else:
                if user_input == 1 and computer_value == 3 or user_input == 2 and computer_value == 1 or user_input == 3 and computer_value == 1:
                    print("you win!")
                else:
                    print("computer wins!")
        else:
            print("invalid digit.")
            invalid_attempts = invalid_attempts - 1
            print(f"you have {invalid_attempts} more attempt(s).")
    else:
        print("invalid input.")
        invalid_attempts = invalid_attempts - 1
        print(f"you have {invalid_attempts} more attempt(s)")
else:
    k = input("you thought you were slick, huh?")


# main
