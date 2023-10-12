"""
Author: Teagan Stewart
Student ID: <w0302952>
Course: PROG1700
Date: September 21st, 2023
Project: Create a simple Algorithm using the program Flowchart and pseudocode
Repository: <https://github.com/teagz17/PROG1700-Algorithms>
Programming Language: Python 3
License: Creative Commons
version 1
"""
import datetime #imports the current date into the script.

current_year = datetime.date.today().year #assigns the current year to the variable.
current_month = datetime.date.today().month #assigns the current month to the variable.

def FindAge(): #defines the function.

    print("welcome to the birth year checker!") #simple greeting.

    while True: #loop
        try:
            birth_month = int(input("please enter the month you were born(1-12): ")) #checks the user's birth month.
            if birth_month < 1 or birth_month > 12:
                print("that's not a valid month. try again: ")
                continue #if the user entered an invalid month, this takes them back to the birth month input.
            else:
                break #if the month is valid, the function continues.
        except ValueError:
            print("whole numbers only. try again: ") #since the birth month's value is supposed to be an integer, any other variable would result in an error.

    while True: #loop
        try:
            age = int(input("please enter your age(whole numbers only): ")) #checks the user's age.
            if age < 0:
                print("that's impossible. enter your actual age: ") #you can't have a negative age.
                continue #same as line 26.
            else:
                break #if the age is valid, the function continues.

        except ValueError:
            print("that's not a whole number. try again: ") #same as line 30.
   
    birth_year = current_year - age #the main formula.

    if current_month < birth_month: #for if the user's birthday hasn't happened yet.
        birth_year = birth_year - 1

    if age > 99:
        print(f"you were born in {birth_year}. you've lived a long life!") #prints the birth year and a message.
    elif age <= 9:
        print(f"you were born in {birth_year}. how did you get here, young fella?") #ditto^
    else:
        print(f"you were born in {birth_year}. cool!") #ditto^

    k = input("thanks for using the birth year finder! press enter to close the window." ) #prevents the window from closing after printing the birth year, pressing enter closes the script.
    

FindAge() #runs the script.