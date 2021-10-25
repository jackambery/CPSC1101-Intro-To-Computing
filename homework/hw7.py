# hw7
# CS 101: Homework #7
# Filename: hw7.py
# Date: 28 Oct 2021
#
# Name: John (Jack) Ambery
#
# A program to simulate an ATM Machine. Practices use of functions.

# balance = 500 (defined in main method)

def printBal(bal):
    print("Your balance is:", bal)

def deposit(bal, amount):
    result = bal + amount
    return result

def withdrawl(bal, amount):
    result = bal - amount
    return result

def menu():
    print("Please type 'a', 'b', 'c', or 'd' for whichever option you desire.")
    print("a) Print balance\nb) make deposit\nc) make withdrawl\nd) quit")

# main method
def main():
    balance = 500
    choice = input("Please type 'a' to start.\n")
    while (choice != 'd'):
        menu()
        if choice == 'a':
            printBal(balance)
        elif choice == 'b':
            amount = int(input("How much would you like to deposit?\n"))
            balance = deposit(balance, amount)
            printBal(balance)
        elif choice == 'c':
            amount = int(input("How much would you like to withdrawl?\n"))
            balance = withdrawl(balance, amount)
            printBal(balance)
        else:
            print("invalid selection")
        choice = input("What would you like to do?\n")
    # if d is selected
    print("Have a nice day!")

if __name__ == "__main__":
    main()