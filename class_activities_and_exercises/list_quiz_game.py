import random #iports the random module
programming_languages = ['python', 'javascript', 'c++', 'ruby', 'java'] #language list
difficulty_levels = [2, 3, 4, 2, 5] #difficulty level list

quiz_data = list(zip(programming_languages, difficulty_levels)) #combines lists and makes them tuples

random.shuffle(quiz_data) #shuffles list for a random quiz order
score = 0
for language, difficulty in quiz_data: #for loop, runs the game
    guess = int(input(f"what is the difficulty level of {language}? (enter a number between 1 and 5):"))
    if guess == difficulty: #if the guess was right
        score += 1 #adds 1 to the total score
        print('correct!')
    else: #if guess was wrong
        print(f'incorrect! the difficulty level of {language} is {difficulty}.')
print(f'\nquiz complete! your final score: {score}/5')