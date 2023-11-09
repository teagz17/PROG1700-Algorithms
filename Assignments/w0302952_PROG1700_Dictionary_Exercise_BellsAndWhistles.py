"""
Teagan Stewart
w0302952
PROG1700
November 9th, 2023
Dictionary exercise
https://github.com/teagz17/PROG1700-Algorithms
Version 2
"""
import sys
student_scores = {
    'luffy': 60,
    'sanji': 84,
    'franky': 93,
    'zoro': 58,
    'jinbe': 76
}
input_attempt = 5

print("1 = show test scores and class average \n2 = view an individual student's test score \n3 = update a student's score \n4 = remove a student and their test score \n5 = view student with the highest score \n6 = exit")
while True:
    while input_attempt > 0:
        try:
            init_input = int(input("what would you like to do? "))
            if init_input >= 1 and init_input <= 6:
                if init_input == 1:
                        average_score = sum(student_scores.values()) / len(student_scores)
                        print('\n'.join("{}: {}".format(k, v) for k,v in student_scores.items()))
                        print(f"class average: {average_score}")
                if init_input == 2:
                    name_input = input("enter student's name: ")
                    if name_input in student_scores:
                            print(f"{name_input}'s test score is {student_scores[name_input]}.")
                    else:
                            input_attempt -= 1
                            print(f"that name isn't in the dictionary. you have {input_attempt} attempts left")
                if init_input == 3:
                    name_input = input("enter student's name: ")
                    if name_input in student_scores:
                        print(f"{name_input}'s current test score is {student_scores[name_input]}.")
                        new_score = int(input(f"please enter {name_input}'s updated score: "))
                        if new_score >= 0 and new_score <= 100:
                            student_scores.update({name_input: new_score})
                            print(f"{name_input}'s new test score is {new_score}.")
                            average_score = sum(student_scores.values()) / len(student_scores)
                            print(f"new class average: {average_score}")
                        else:
                            input_attempt -= 1
                            print(f"invalid input. you have {input_attempt} attempts left")
                    else:
                        input_attempt -= 1
                        print(f"that name isn't in the dictionary. you have {input_attempt} attempts left")
                if init_input == 4:
                    name_input = input("type the name of the student you would like to remove from the dictionary: ")
                    if name_input in student_scores:
                        del student_scores [name_input]
                        print(f"{name_input} has been removed from the dictionary.")
                        average_score = sum(student_scores.values()) / len(student_scores)
                        print(f"new class average: {average_score}")
                    else:
                        input_attempt -= 1
                        print(f"that name isn't in the dictionary. you have {input_attempt} attempts left")
                if init_input == 5:
                    high_score = max(zip(student_scores.values(), student_scores.keys()))
                    print (f"this student currently has the highest test score: {high_score}")
                if init_input == 6:
                    sys.exit()
            else:
                input_attempt -= 1
                print(f"invalid input. you have {input_attempt} attempts left")
        except ValueError:
            input_attempt -= 1
            print(f"invalid input. you have {input_attempt} attempts left")
    else:
        input("too many invalid inputs. try again later")
        break