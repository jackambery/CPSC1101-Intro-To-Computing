# Homework #10
# CS 101: File Reading
# Filename: fileReading.py
# Date: 2 December 2021
#
# Name: John (Jack) Ambery
#
# A class to read, write, and append to a file.

import csv

class FileReader:

    def __init__(self):
        self.outputFile = "homework\hw10\\result.txt"
        self.outputFileCSV = "homework\hw10\\resultCSV.csv"
    
    def __repr__(self):
        print("I write, read, and append to files!")

    def write(self, message):
        with open(self.outputFile, "w") as outfile:
            outfile.write(message)

    def read(self):
        with open(self.outputFile, "r") as outfile:
            print(outfile.read())

    def append(self, message):
        with open(self.outputFile, "a") as outfile:
            outfile.write(message)

    def writeCSV(self, list):
        with open(self.outputFileCSV, "w", newline = "") as outfile:
            writer = csv.writer(outfile)
            writer.writerows(list)

    def readCSV(self):
        with open(self.outputFileCSV, newline = "") as outfile:
            reader = csv.reader(outfile)
            for row in reader:
                for val in row:
                    print(val + ", ")

    def appendCSV(self, list):
        with open(self.outputFileCSV, "a", newline = " ") as outfile:
            writer = csv.writer(outfile)
            writer.writerows(list)
