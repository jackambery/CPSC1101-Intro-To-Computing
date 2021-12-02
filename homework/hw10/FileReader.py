# Homework #10
# CS 101: File Reading
# Filename: fileReading.py
# Date: 2 December 2021
#
# Name: John (Jack) Ambery
#
# A class to read, write, and append to a file.

class FileReader:

    def __init__(self):
        self.outputFile = "homework\hw10\\result.txt"
    
    def __repr__(self):
        print("I write, read, and append to files!")

    def write(self, message):
        outfile = open(self.outputFile, "w")
        outfile.write(message)

    def read(self):
        outfile = open(self.outputFile, "r")
        print(outfile.read())

    def append(self, message):
        outfile = open(self.outputFile, "a")
        outfile.write(message)

    def writeCSV(self):
        return

    def readCSV(self):
        return

    def appendCSV(self):
        return