# hw2
# CS 101: Homework #2
# Filename: hw2.py
# Date: 16 Sept 2021
#
# Name: John (Jack) Ambery
#
# A program to explore the ways one can manipulate strings using built in python functions

#q1
myName = "jack ambery"
print(myName)
print(len(myName))
print(myName * 5)

#q2
coolFact = "I have experience playing the BANJO"
print(myName + coolFact)

#q3
print(myName.upper())
print(coolFact.lower())

#q4
print("The first character of my name is:", myName[0])
print("The second character of my name is:", myName[1])
print("The last character of my cool fact is:", coolFact[len(coolFact) - 1])
print("The second to last character of my cool fact is:", coolFact[len(coolFact) - 2])

#q5
print("The middle character of my name is:", myName[int(len(myName) / 2)]) # have to cast to int if len(str) is odd

#q6
print("My sliced up name(first 9 chars) is:", myName[:9:2])

#q7
age = 18
print("My name is " + myName + ". I am " + str(age) + " years old.")