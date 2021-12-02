

from FileReader import FileReader
from homework.hw7 import menu

class FileTest:

    def menu():
        print("Please type '1', '2', '3', '4', '5', '6', or '7' for whichever option you desire.")
        print("1) Write to the file.\n2) Read the file.\n3) Append to the file.\n4) Write to the CSV file.\n5) Read the CSV file.\n6) Append to the CSV file.\n7) Quit")

    def main():

        theReader = FileReader()
        theReader.write("Hello world!!!!!!!!!!!!!!!!")

        while (True):
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