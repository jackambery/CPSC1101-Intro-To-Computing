# Lab 2
# CS 101: Lab #2
# Filename: lab2.py
# Date: 27 Sept 2021
#
# Name: John (Jack) Ambery
# A lab to practice user input and contional statements
# This program is a number guesser game that will prompt the user for
# five guesses, telling them if their guess is higher, lower, or equal
# to the randomly generated integer (1-99)

import random

answer = random.randint(1, 99)
print("I am thinking of a number 1 through 99.\nTry and guess it!")

#while loop
guessCount = 1
while guessCount <= 6:
    if guessCount == 6:
        print("you did not guess my number. sorry, try again.\nMy number was:", answer)
        break
    guess = int(input("What is guess #" + str(guessCount) + "?\n"))

    if guess == answer:
        print("winner winner chicken dinner!")
        print("My number was:", answer)
        break
    elif answer - guess == 1 or answer - guess == -1:
        print("wow you are super close!")
    elif answer - guess > 1:
        print("Your guess is too small!")
    elif answer - guess < -1:
        print("Your guess is too big!")
    
    guessCount += 1

#for loop
for i in range(1, 6):
    if i == 6:
        print("you did not guess my number. sorry, try again.\nMy number was:", answer)
        break
    guess = int(input("What is guess #" + str(i) + "?\n"))

    if guess == answer:
        print("winner winner chicken dinner!")
        print("My number was:", answer)
        break
    elif answer - guess == 1 or answer - guess == -1:
        print("wow you are super close!")
    elif answer - guess > 1:
        print("Your guess is too small!")
    elif answer - guess < -1:
        print("Your guess is too big!")