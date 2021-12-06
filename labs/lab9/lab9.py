# Lab 9
# CS 101: Lab #9
# Filename: lab9.py
# Date: 6 Dec 2021
#
# Name: John (Jack) Ambery
# A lab to practice recursion

# q1
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

def nthTriangle(n):
    if n == 0:
        return n
    else:
        return n + nthTriangle(n - 1)

def palindrome(s, startIndex, endIndex):
    if endIndex == 0:
        return True
    if s[startIndex] != s[endIndex]:
        return False
    else:
        return palindrome(s, startIndex + 1, endIndex - 1)


print("4 factorial:", factorial(4))
print("3 Nth Triangle:", nthTriangle(3))

myPalindrome = "panama"
print(myPalindrome + " is a palindrome: " + str(palindrome(myPalindrome, 0, len(myPalindrome) - 1)))

myPalindrome = "racecar"
print(myPalindrome + " is a palindrome: " + str(palindrome(myPalindrome, 0, len(myPalindrome) - 1)))