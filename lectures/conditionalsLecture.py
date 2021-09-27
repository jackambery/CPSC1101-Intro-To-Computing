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

#reminder: indentation is important (unlike java)

#you can nest loops:
x = 10
y = 12
if x < y:
    print("x is less than y")
else:
    if y > 20:
        print("y is bigger than 20")
    else:
        print("y is bigger than x but less than 20")


#chained contionals 
z = 990

if z < 5:
    print("z is small")
elif z < 60:
    print("x is kinda big")
else:
    print("z is huge")


#more for loops
for i in range(5, 10):
    print("i is:", i)


#for loop over list (array)
names = ["jeff", "jack", "john", "jim"]
for name in names:
    print(name)


#while loops
index = 0
while index < 5:
    print(index)
    index += 1

#break
for i in range(0, 10):
    if (i == 4):
        break

    print("i is:", i)

#continue
for i in range(0, 10):
    if (i == 4):
        continue
    
    print("i is:", i)