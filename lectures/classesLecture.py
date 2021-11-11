'''
Classes are user made data structures

objects refer to themselces as 'self'

every class has:
    __init__ == constructor
    __repr__ == tells python how to print the class/object
'''

class Phone:

    def __init__(self, number, brand, color):
        self.number = number
        self.brand = brand
        self.color = color
    
    def __repr__(self):
        s = "**Your phone info**"
        return s