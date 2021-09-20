# 20 Sept 2021
#
# Name: John (Jack) Ambery
# 
# Following along a lecture about operators and operands

'''
operators - the special characters to do computations/functions
operands - the values to be used

() parens
** power
- negate
*, %, / multiply, modulus, divide
+, - add, subtract
> == < compare
= assign

'''
var1 = (5 + 9) * (15 - 7)
print(var1)

var2 = var1 + 32   # variable plus literal
print(var2)

powVar = var2 ** 4
print(powVar)

#modulus examples
print("40%6 =", 40%6)
print("40%2 =", 40%2)
# use mod 2 to determine odd/even numbers

#input function:
# input function must be used to define a variable
userNum = int(input("Please enter a number: ")) # note that input is a String until you cast it
print("Your number plus 10 is:", userNum + 10)