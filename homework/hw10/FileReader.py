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

    # this function uses (optional) try and except statements
    # since I use a class varible for the file names, it should never reach those,
    # but it would have been good to use them from the start
    def read(self):
        try:
            
            with open(self.outputFile, "r") as outfile:
             print(outfile.read())
        
        except FileNotFoundError as f:
            print("no file: ", str(f))
        except Exception as e:
            print("error:", str(e))

    def append(self, message):
        with open(self.outputFile, "a") as outfile:
            outfile.write(message)

    # right now this method does not take user input and has a pretyped set of data
    # to test the method
    def writeCSV(self):

        csvRow = ['Name', 'Age', 'Major']
        students = [
            ['Jack', '19', 'Comp Sci'],
            ['Joe', '17', 'Mech. Engineering'],
            ['Em', '20', 'English']
        ]

        with open(self.outputFileCSV, "w", newline = "") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(csvRow)
            writer.writerows(students)

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
