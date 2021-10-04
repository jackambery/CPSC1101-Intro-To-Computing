# hw4
# CS 101: Homework #4
# Filename: hw4.py
# Date: 4 Oct 2021
#
# Name: John (Jack) Ambery
#
# A program to practice list manipulation

import copy

#a
list = ["bear", "lizard", "koala", "frog", "deer"]
print("My original list:", list)


#b
print("This is the second item in my list:", list[1])

#c
list[3] = "many frogs"
print(list)

#d
for animal in list:
    print(animal)

#e
for animal in list:
    if(animal == "lizard"):
        print(animal)

#f
print("The length of my list is:", len(list))

#g
list.append("rabbit")
print("My list with new item:", list)

#h
list.insert(1, "goldfish")
print("My list with new item at 2nd pos:", list)

#i
birds = ["goose", "turkey", "cardinal"]
list.insert(3, birds)
print("My list with birds:", list)

#j
list.remove("many frogs")
print("No more frogs:", list)

#k
list.remove(list[2])
print("3rd element gone:", list)

#EC
#a
list2 = ['house', 'tree', 'kite', 'axe', 'cow']

copyList = copy.deepcopy(list2)
print(list2)
print("deep copy:", copyList)

list2.sort()
print("sorted:", list2)

list2.reverse()
print("reversed:", list2)

list2.clear()
print("cleared:", list2)