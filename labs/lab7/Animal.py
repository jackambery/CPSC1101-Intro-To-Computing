# Lab 7
# CS 101: Lab 7
# Filename: Animal.py
# Date: 15 November 2021
#
# Name: John (Jack) Ambery
#
# A lab for practicing communication between classes

class Cat():

    def __init__(self, name, breed, meowSound, milkPreference):
        self.name = name
        self.breed = breed
        self.meowSound = meowSound
        self.milkPerference = milkPreference

    def __repr__(self):
        s = "I am a " + self.breed + " cat named " + self.name + ". " + self.meowSound
        if self.likesMilk() == True:
            s += ". I do like milk."
        else:
            s += ". I do not like milk."
        return s
    
    def likesMilk(self):
        return self.milkPerference
    
    def updateMeow(self, sound):
        self.meowSound = sound