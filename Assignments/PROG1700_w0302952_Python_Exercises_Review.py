'''
w0302952
teagan stewart
Python Exercises Review
November 27th, 2023
'''

# strings
    # concatenation
str1 = "hello, "
str2 = "world!"
result_str = str1 + str2
print(result_str)

    # substring
substr = "the one piece is real"
print(substr[0:5])

    # formatting
str_f = "the coordinates are {}, {}, {}."
print(str_f.format(263, 35, -160))

# loops 
    # print numbers
for i in range(1,11):
    print(i)

    # factorial
n = 5
fac = 1
result = 1
while fac <= n:
    result *= fac
    fac += 1
print(result)

# sets
    # intersection
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersectionset = set1.intersection(set2)
print(intersectionset)

    # union
unionset = set1.union(set2)
print(unionset)

    # difference
diffset = set1.difference(set2)
print(diffset)

# lists:
    # list operations
list1 = [1, 2, 3, 4, 5, 6]
print(sum(list1))
print(sum(list1)/len(list1))
print(max(list1), min(list1))

    # list comprehension
squares = [x**2 for x in range(1, 11)]
print(squares)

# tuples
    # tuple unpacking
tupl1 = ("tequila", "triple-sec", "lime")
(one, two, three) = tupl1
print(one)
print(two)
print(three)

# dictionaries
    # dictionary operations
dict1 = {"name": "teagan", "age": 25, "city": "inverness"}
for key, value in dict1.items():
    print(f"{key}: {value}")

    # nested dictionary
dict2 = {
    "joe": {"gr1": 89, "gr2": 93},
    "wayne": {"gr1": 94, "gr2": 98}
}

for student, grades in dict2.items():
    avg_grade = sum(grades.values()) / len(grades)
    print(f"{student}'s average grade: {avg_grade}")

# functions
    # function basics
def myFunc(x, y):
    print(x+y)

myFunc(20, 30)

    # default values
def myFunc2(x = 60, y = 40):
    print(x+y)

myFunc2()

# reading/writing external files
    #file reading
z = open("sample.txt", "r")
print(z.read())

    #file writing
a = open("output.txt", "x")

b = open('output.txt', 'w')
b.write('test')
b.close()

c = open('output.txt', 'r')
print(c.read())