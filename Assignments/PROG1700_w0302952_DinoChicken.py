"""
teagan stewart
w0302952
PROG1700
Fried Chicken Dinosaur
October 19th, 2023
https://github.com/teagz17/PROG1700-Algorithms
version 1
"""
chicken_in_box = float(20)
day_counter = int(0)
chicken_eaten_daily = float(0)
chicken_eaten_while_ill = int(0)

print("the dinosaur starts with 20lbs of chicken. on the first day he eats 1 lb, then eats 5% more each day.")
while chicken_in_box > 0:
    day_counter += 1
    chicken_eaten_daily += chicken_eaten_daily * .05
    if day_counter == 1:
        chicken_eaten_daily = 1
        chicken_in_box -= 1
        print(f"fried chicken eaten on day {day_counter} = {chicken_eaten_daily} lb")            
        print(f"fried chicken remaining = {round(chicken_in_box, 2)} lbs")
    elif day_counter == 7:
        print(f"fried chicken eaten on day {day_counter} = {chicken_eaten_while_ill} lbs (he was sick today.)")
        print(f"fried chicken remaining = {round(chicken_in_box, 2)} lbs")
    elif chicken_eaten_daily > chicken_in_box:
        print(f"fried chicken eaten on day {day_counter} = {round(chicken_in_box, 2)} lbs. that's the last of it!")
        chicken_in_box = 0
        print(f"it took {day_counter} days to run out of chicken.")
    else: 
        chicken_in_box -= chicken_eaten_daily
        print(f"fried chicken eaten on day {day_counter} = {round(chicken_eaten_daily, 2)} lbs")
        print(f"fried chicken remaining = {round(chicken_in_box, 2)} lbs")