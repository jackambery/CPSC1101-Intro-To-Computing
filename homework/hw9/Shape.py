# Homework #9
# CS 101: Square Main Class
# Filename: square.py
# Date: 18 November 2021
#
# Name: John (Jack) Ambery
#
# A class that defines a square and the necessary and associated methods

class Square:
    def __init__(self, length, color):
        self.length = int(length)
        self.color = color

    def __repr__(self):
        s = "Hello I am a square. My sides are " + str(self.getSide()) + " units long and I am " + self.getColor() + "."
        return s

    #returns int
    def getSide(self):
        return self.length

    #returns int
    def getArea(self):
        return self.length * self.length

    #returns int
    def getPerimeter(self):
        return 4 * self.length

    def setColor(self, newColor):
        self.color = newColor

    def getColor(self):
        return self.color

    def describe(self):
        return "I am a " + self.getColor() + " square with a side length of " + str(self.getSide()) + "."
        # return self.__repr__ ?

    