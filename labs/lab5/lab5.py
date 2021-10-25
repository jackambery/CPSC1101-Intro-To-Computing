# Lab 5
# CS 101: Lab #5
# Filename: lab5.py
# Date: 25 Oct 2021
#
# Name: John (Jack) Ambery
# A lab to practice functions

def helloWorld():
    print("hello world")

def goodDay(name):
    s = "good day, " + name
    return s

def length(s):
    return len(s)

def isEven(num):
    if num % 2 == 1:
        return False
    else:
        return True

def reverse(s):
    reversed = s[::-1]
    return reversed

def helper(s):
    return 'gday, mate ' + s

def primary(name):
    withHelper = helper(name)
    wholeMessage = withHelper + ' see, ya'
    return wholeMessage

def main():
    helloWorld()

    myString = goodDay("Professor Kramer")
    print(myString)

    intLength = length("jack ambery")
    print("The length of my name:", intLength)

    bool34 = isEven(34)
    print("Is 34 even?:", bool34)
    bool101 = isEven(101)
    print("Is 101 even?:", bool101)

    reverseName = reverse("jack ambery")
    print("The reverse of my name:", reverseName)

    message = primary("Professor Kramer")
    print(message)


if __name__ == "__main__":
    main()