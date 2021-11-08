
'''
methods to help go back and fourth between ascii and decimal:
chr - takes a number, give a char
ord - takes a letter, gives a number

SDLC = Software Development Life Cycle
    1. Visualize
    2. Break Up
    3. Compose
'''

def fun1():
    print(ord('U') / 2)
    print(chr(ord('i') + 13))

def main():
    fun1()

if __name__ == "__main__":
    main()