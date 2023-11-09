"""
Teagan Stewart
w0302952
PROG1700
November 9th, 2023
Dictionary exercise
https://github.com/teagz17/PROG1700-Algorithms
Version 1
"""
# Create an empty dictionary

student_scores = {}

# Add student names and scores to the dictionary

student_scores = {
    'luffy': 60,
    'sanji': 84,
    'franky': 93,
    'zoro': 58,
    'jinbe': 76
} 

# Print the initial dictionary

print('\n'.join("{}: {}".format(k, v) for k,v in student_scores.items())) # this line prints each key and value individually, without the brackets and quotations

# Calculate and print the average score

average_score = sum(student_scores.values()) / len(student_scores)
print(f"class average: {average_score}")

# Prompt user for a student's name and check if the student exists

name_input = input("enter student's name: ")
if name_input in student_scores:
    print(f"{name_input}'s test score is {student_scores[name_input]}.")

# Update a student's score

name_input = input("enter student's name: ")
if name_input in student_scores:
    print(f"{name_input}'s current test score is {student_scores[name_input]}.")
    new_score = int(input(f"please enter {name_input}'s updated score: "))
    student_scores.update({name_input: new_score})
    print("updated scores:")
    print('\n'.join("{}: {}".format(k, v) for k,v in student_scores.items()))
    average_score = sum(student_scores.values()) / len(student_scores)
    print(f"new class average: {average_score}")

# Remove a student from the dictionary

name_input = input("type the name of the student you would like to remove from the dictionary: ")
if name_input in student_scores:
    del student_scores [name_input]
    print(f"{name_input} has been removed from the dictionary.")
    print("updated scores:")
    print('\n'.join("{}: {}".format(k, v) for k,v in student_scores.items()))
    average_score = sum(student_scores.values()) / len(student_scores)
    print(f"new class average: {average_score}")

# Calculate and print the highest score and student

high_score = max(zip(student_scores.values(), student_scores.keys()))
print (f"this student currently has the highest test score: {high_score}")