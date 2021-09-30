# 30 Sept 2021
#
# Name: John (Jack) Ambery
# 
# Following along a lecture about lists

l = ["apple", "cherry", "banana"] # indexes are 0, 1, 2
print(l)
print(l[0])
print(l[1])
print(l[2])

l2 = ["chips", "nuts", "pretzels"]

l = ["apple", "cherry", l, "banana"]
print(l) #list with sublist

#index based access
condoments = ["mustard", "mayo", "relish"]
print("ketchup" in condoments) # use "in" to see if an item is in a list, this returns false

#concatenate lists
print(l2 + condoments)

# you can slice through/reverse a list just like you can with a string
print(l2[::-1])

'''
methods:
- append - adds an element to the end of a string (item)
- insert - inserts item to certain spot in list (index, item)
- pop - removes and returns the last item in list (none)
- pop - removes and returns specific item in list (index)

'''