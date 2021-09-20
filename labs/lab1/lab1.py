# Lab 1
# CS 101: Lab #1
# Filename: lab1.py
# Date: 20 Sept 2021
#
# Name: John (Jack) Ambery
# A lab to practice user input, operators, and String manipulation

#q1
userNum1 = int(input("Please enter the first number: "))
userNum2 = int(input("Please enter the second number: "))
result = userNum1 * userNum2
print("The product of the two numbers:", result)

#q2
userString = input("Please enter a String:")
print("The length of the String is:", len(userString))

#q3
userAge = int(input("Please enter your age: "))
print("In ten years, you will be " + str(userAge + 10) + " years old.")

#q4
userString2 = input("Please enter another String: ")
print("The String is:", userString2)
print("The first and last characters of the String are:", userString2[:1], userString2[len(userString2) - 1])

#q5
myString = '!!!!!'
print(myString * 10)

#q6
modNum = int(input("Please enter a number: "))
print("Your number mod 2 is:", modNum % 2)

'''
if modNum % 2 == 0:
    print("Your number is even!")

else:   # if modNum % 2 == 1
    print("Your number is odd!")
'''