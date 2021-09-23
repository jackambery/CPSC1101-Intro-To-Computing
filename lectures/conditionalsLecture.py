# 23 Sept 2021
#
# Name: John (Jack) Ambery
# 
# Following along a conditionals lecture

#if/else

x = int(input("Enter an integer:"))
if x % 2 == 0:
    print(x, "is even.")
else:
    print(x, "is false.")

if x < 0:
    print("The negative number", x, "is not valid here.")
print("This is always printed")


#for

for x in range(6,20):
    print(x)