# 16 Sept 2021
#
# Name: John (Jack) Ambery
# 
# Following along a string lecture

'''
bit = 1 or 0
byte = 8 bits
kilobyte = 1,000 or 2^10 bytes
megabyte = 1,000 kilobytes
gigabyte = 1,000 megabytes

variable = a storage unit

'''
name1 = "even steven"
name2 = "odd todd"
num1 = 35
num2 = 45

print("val of num2 =", num2)

num2 = 9999

print("val of num2 is now:", num2)

'''
datatypes are "implicit" in python
- this means no datatype declaration is needed
- no such thing as double in python, use float

'''
print(1 / 5) #still gives you a float even though not specified

#updating variables
carModel = "yugo"

print("My car model now is a", carModel)
carModel = "tesla"
carModel = carModel + " the 1995 version"
print("My car is now a", carModel)

var1 = 10
var1 = var1 - 5

#casting + concatenation
str1 = "my grandpa is "
str2 = "dave"
num3 = 88
print(str1 + str2)
print(str1 + str2 + ", he is " + str(num3)) #concatenating strings


#naming convention
'''
- make sure variables are camelCase
- no variables names can be keywords
    - like print, str, class
'''
'''
- a string literal is a string that is now a part
    of a variable, it is just printed in a print
    statement
- single quotes and double quotes are interchangable
'''

#string functions
str3 = 'jack ambery'
print(str3)
print(len(str3)) # gives you an integer length of the string
print(str3 * 4) # repeats the string
print (str3.upper()) # to uppercase
print(str3.count('jack')) # counts the instances of given substring

#indexes
count = 1
for x in str3:
    print(x)
    count += 1

print(count)

#you can print the negative index
print('the last letter of my name is:', str3[-1])

#substings and how they work (slicing and skipping)
'''
string[start:stop:step]
'''
str4 = 'sundays we play tennis only if the weather is good'
print(str4)
print("first 5 letters:", str4[0:5])
print("letter 7 to the end:", str4[7:])
print("letter 7 to the end again:", str4[7:len(str4)])
print('reverse:', str4[::-1])

#skipping
print('stride by 2:', str4[::2]) #two blanks indicate start and end
