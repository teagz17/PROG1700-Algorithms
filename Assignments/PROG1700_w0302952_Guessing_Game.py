"""
Teagan Stewart
w0302952
PROG1700
October 11th, 2023
Guessing Game assignment
Programming Language: Python 3
Version 1
"""
import random # imports the random module

# variables
attempts = 1 # sets the amount of attempts the user can make before the program closes
computer_value = random.randrange(1,11,1) # generates a random number betwee 1 and 10. outside of the while loop so that the number stays the same each round

user_name = str(input("welcome to the guessing game! please enter your name: ")) # asks the user their name
print(f"welcome, {user_name}! i'm thinking of a number between 1 and 10. can you guess what it is in five attempts or less?") # greets the user and explains the game

while attempts <= 5: # starts the loop
    print(f"attempt {attempts}/5.")
    user_input = input("enter your guess (whole numbers only): ")
    if user_input.isdigit(): # user can only enter numbers
        user_input = int(user_input) # user can only enter whole numbers
        if user_input >=1 and user_input<= 10: # user can only enter numbers betweeen 1 and 10
            if user_input == computer_value: # user wins
                print("you're right, good job!")
                print(f"you got the right answer after {attempts} attempt(s).") # shows how many attempts it took to get the right guess
                attempts = 6 # ends the loop
            else:
                attempts = attempts + 1 # user has one less try
                if user_input < computer_value: # gives the user hints
                    if attempts > 5:
                        print(f"the number was {computer_value}.")
                    else:
                        print("close, but not quite! maybe it's higher than that...")
                if user_input > computer_value:
                    if attempts > 5:
                        print(f"the number was {computer_value}.")
                    else:
                        print("nope, try again! maybe try a lower number next time...")
        else:
            attempts = attempts + 1 # lowers remaining attempts if user tries to input a number less that 1 or greater than 10
            print("invalid digit, pick between 1 and 10.")
            print(f"attempt {attempts}/5")
    else:
        attempts = attempts + 1 # lowers remaining attempts if user tries to input anything that isn't an integer
        print("invalid input. please enter a whole number.")
        print(f"attempt {attempts}/5")
else: # end of the game, prints different messages depending on the outcome
    if user_input == computer_value: # prints if the user wins
        input(f"thanks for playing, {user_name}!")
    else: # prints if the user runs out of attempts
        input(f"better luck next time, {user_name}!")