import datetime

current_year = 0
age = 0
birth_year = 0
mainloop = 3
loop_counter = 0

while loop_counter < mainloop:

    age_input = input("Please enter your age (numbers only): ")

    if age_input.isdigit():
        age = int(age_input)
        current_year = datetime.datetime.now().year
        birth_year = current_year - age
        print("you were born in the year", birth_year, ".")

    else:
        print("invalid input. plase enter your age using numbers only.")
    
    loop_counter = loop_counter + 1

else:
    print("you have", mainloop, "attempts.")
