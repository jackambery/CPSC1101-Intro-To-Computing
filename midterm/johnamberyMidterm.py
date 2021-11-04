# Name: John (Jack) Ambery
# Date: 1 November 2021
# --- MIDTERM ---

#q1
firstName = input("Please enter your first name:\n")
lastName = input("Please enter your last name:\n")

def printName(first, last):
    fullName = first + " " + last
    print("Hello " + fullName + "! You just delved into python.")

printName(firstName, lastName)

#q2
multi = "Hello I am a multi word string"

def splitter(phrase):
    wordList = phrase.split(" ")
    newPhrase = ""
    for word in wordList:
        newPhrase = newPhrase + word + "-*-"
    newPhrase = newPhrase[:len(newPhrase) - 3] # removes trailing "-*-"
    return newPhrase

print(splitter(multi))

#q3
userInt = int(input("Please enter an integer:\n"))
x = 0
while x < userInt:
    print(x ** 2)
    x += 1

#q4
userYear = int(input("Please enter a year to see if it is a leap:\n"))

def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False    
    elif year % 4 == 0:
        return True
    else:
        return False

print(str(userYear) + " is a leap year: " + str(isLeapYear(userYear)))

# test cases
print("2100 is a leap year: " + str(isLeapYear(2100)))
print("2400 is a leap year: " + str(isLeapYear(2400)))

#q5
woodchuck = "how much wood could a wood chuck chuck if a wood chuck could chuck wood test test test test test test"
words = woodchuck.split()

def dictMaker(wordList):
    dict = {}
    for word in wordList:
        if dict.get(word) == None:
            dict.update({word : 1})
        else:
            dict[word] += 1
    return dict

print(dictMaker(words))

#q6
'''
            ------ PSEUDOCODE ------
keys = names
vals = 3 numbers == marks for math, physics, chem

get an int from user -> numStudents

in a loop that happens numStudents times:
    get name from user and threee marks from user, seperated by spaces
        split this input on spaces
        first item will be key
        rest will make this a variable to be used for the val
    add to the dict: name with the mark array as the val

dict is now full and complete
'''

def makeDict():
    numStudents = int(input("Please enter the number of students to be added (2 to 10):\n"))
    count = 1
    dict = {}
    while count <= numStudents:
        entry = input("Please enter the name and marks of Student #" + str(count) + ":\n")
        list = entry.split()
        dict.update({list[0]:list[1:]})
        count += 1
    return dict

def getAverage(dict, student):
    total = 0
    for num in dict.get(student):
        total = total + int(num)
    return total / 3.0

#if i had more time, this would be broken into a few more lines
students = makeDict()
print("That person's average is:", getAverage(students, input("Who would you like the average grade of?:"))) 