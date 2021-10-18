# Lab 4
# CS 101: Lab #4
# Filename: lab4.py
# Date: 18 Oct 2021
#
# Name: John (Jack) Ambery
# A lab to practice dictionaries

#q1
guitarists = {
    "Jimi Hendrix": "Little Wing",
    "David Gilmore": "Wish You Were Here",
    "Stevie Ray Vaughn": "Lenny"
}
print("My dictionary:", guitarists)

print("My favorite Hendrix song is:", guitarists.get("Jimi Hendrix"))

print("Is David Gilmore found in this dictionary?:")
if "David Gilmore" in guitarists:
    print("true")
else:
    print("false")

guitarists2 = guitarists.copy()
print("Copied dictionary:", guitarists2)
print("Original dictionary:", guitarists)

guitarists2.clear()
print("Empty dictionary:", guitarists2)

#q2
fourScore = "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal test test test test test"
wordDictionary = {}
words = fourScore.split()
for word in words:
    if wordDictionary.get(word) == None:
        wordDictionary.update({word : 1})
    else:
        wordDictionary[word] += 1

print(wordDictionary)