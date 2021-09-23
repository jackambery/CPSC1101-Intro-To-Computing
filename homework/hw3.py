# hw3
# CS 101: Homework #3
# Filename: hw3.py
# Date: 23 Sept 2021
#
# Name: John (Jack) Ambery
#
# A program to practice the use of conditional statements and loops

#q1a
a = 1
while a <= 12:
    print(a)
    a += 1

#q1b
for x in range(1,13):
    print(x)

#q2
q2 = 1
while q2 <= 12:
    if (q2 % 2) == 1:
        print(q2)
    q2 += 1

#q3
q3 = input("Please enter a word:")
print(q3[::-1])

#q4
password = input("Please enter your password: ")
if len(password) > 17 or len(password) < 6:
    print("Unable to change password: must be between 6 and 16 characters")

lower = False
upper = False
num = False
special = False

for char in password:
    if char.islower():
        lower = True
    if char.isupper():
        upper = True
    if char.isdigit():
        num = True
    if char == '$' or char == '#' or char == '@':
        special = True

if lower == False:
    print("You need a lowercase letter in your password.")
if upper == False:
    print("You need an uppercase letter in your password.")
if num == False:
    print("You need a number in your password.")
if special == False:
    print("You need a special character ($, #, @) in your password.")

if lower and upper and num and special:
    print("Password successfully changed!")

#q5
count = 0
while count <= 50:
    if count % 3 == 0 and count % 5 != 0:
        print("bizz")
    if count % 5 == 0 and count % 3 != 0:
        print("buzz")
    if count % 5 == 0 and count % 3 == 0:
        print("bizzbuzz")
    if count % 3 != 0 and count % 5 != 0:
        print(count)
    count += 1