# Lab 3
# CS 101: Lab #3
# Filename: lab3.py
# Date: 4 Oct 2021
#
# Name: John (Jack) Ambery
# A lab to practice list manipulation

'''
Pseudecode:
1) Create empty list
2) In a loop that will happen five times, ask the user for a new kind of candy AND append it to the list
3) ask the user for a candy to delete from the list, use list remove method to get rid of it
4) append a new user input to the list, this will be another type of candy
5) use list sort method to sort the list into alphabetical order
6) in a for loop, append in reverse order, all elements to a new list
'''

candyList = []

for i in range(0, 5):
    candyList.append(input("Please enter a new candy!:"))
print("Your selection of " + str(len(candyList)) + " candies is:", candyList)

candyList.remove(input("What candy would you like to delete from the list?\n"))
print("Your selection:", candyList)

candyList.append(input("What new candy would you like to add to the list?\n"))
print("Your selection:", candyList)

candyList.sort()
print("This is your sorted list:", candyList)

candyList.reverse()
print("This is your reversed sorted list:", candyList)
