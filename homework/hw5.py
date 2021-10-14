# hw5
# CS 101: Homework #5
# Filename: hw5.py
# Date: 7 Oct 2021
#
# Name: John (Jack) Ambery
#
# A program to practice list manipulation

import random
import copy

#q1
beaches = [] # each beach has a: name, body of water type, salt/freshwater, size of waves(small/medium/large)
beaches.append(["Second Beach", "ocean", "saltwater", "medium"])
beaches.append(["Potomac River Park", "river", "freshwater", "small"])
beaches.append(["Waimea Bay", "ocean", "saltwater", "large"])
beaches.append(["Praia De Norte", "ocean", "saltwater", "large"])
beaches.append(["Bellarmine Pond", "pond", "freshwater", "small"])
beaches.append(["Corolla Beach", "ocean", "saltwater", "medium"])

#q1a
print(beaches)

#q1b
for beach in beaches:
    print(beach)

#q1c
for beach in beaches:
    print("At " + beach[0] + ", the waves are " + beach[3])
print("\n")

#q2
randNums = []
i = 0
while i < 5:
    randNums.append(random.randrange(0, 100))
    i += 1

print("The list of random numbers (1-100):", randNums)
randNums.sort()
print("The minimum value:", randNums[0])
print("The maximum value:", randNums[4])
print("A random value:", random.choice(randNums))
random.shuffle(randNums)
print("The shuffled list:", randNums)
print("\n")

#q3
breakfast = ["bacon", "pancakes", "eggs", "french toast", "grape nuts"]
lunch = copy.copy(breakfast)
lunch[0] = "ham"
lunch[2] = "waffle"
print("First list:", breakfast)
print("Second list:", lunch)
print("\n")

#q4
desserts = ["ice cream", "brownie", "cake", "cookie", "candy"]
moreDesserts = copy.deepcopy(desserts)
moreDesserts[0] = "ice cream sundae"
moreDesserts[2] = "pie"
print("First list:", desserts)
print("Second list:", moreDesserts)
print("\n")

#q5
softDrinks = ["coca cola", "sprite", "root beer", "mountain dew", "crush"]
softerDrinks = softDrinks
softerDrinks[0] = "pepsi"
softerDrinks[1] = "7-up"
print("First list:", softDrinks)
print("Second list:", softerDrinks)