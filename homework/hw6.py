# hw6
# CS 101: Homework #6
# Filename: hw6.py
# Date: 14 Oct 2021
#
# Name: John (Jack) Ambery
#
# A program to practice dictionaries and retrieving values from them

vaca_supplies = ["sunscreen", "swimsuit", "hat", "shades"]

stock = {
    "sunscreen": 3,
    "hat": 0,
    "swimsuit": 2,
    "shades": 15    
}

prices = {
    "sunscreen": 4,
    "hat": 2,
    "swimsuit": 18.5,
    "shades": 11
}

total = 0
for item in vaca_supplies:
    total += prices[item]
print("Total for all possible items:", total)

total = 0 # reset total for second loop
for item in vaca_supplies:
    if stock[item] > 0:
        total += prices[item]
        stock[item] -= 1

print("Total for all items in stock:", total)
print("What is left in stock:", stock)
