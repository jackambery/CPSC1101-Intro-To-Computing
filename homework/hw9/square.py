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
        self.length = length
        self.color = color

    def __repr__(self):
        s = "Hello I am a square. My sides are " + str(self.length) + " units long and I am " + self.color
        return s

    def getSide(self):
        return self.length

    def getArea(self):
        return int(self.length) * int(self.length)

    def getPerimeter(self):
        return 4 * int(self.length)

    def setColor(self, newColor):
        self.color = newColor

    def getColor(self):
        return self.color

    def describe(self):
        return repr(self)

    