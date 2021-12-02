

from FileReader import FileReader
from homework.hw7 import menu

class FileTest:

    def menu():
        print("Please type '1', '2', '3', '4', '5', '6', or '7' for whichever option you desire.")
        print("1) Write to the file.\n2) Read the file.\n3) Append to the file.\n4) Write to the CSV file.\n5) Read the CSV file.\n6) Append to the CSV file.\n7) Quit")

    def main():

        theReader = FileReader()

        while (True):
            menu()
            if choice == '1':
                message = input("What would you like to write?\n")
                theReader.write(message)
            elif choice == '2':
                theReader.read()
            elif choice == '3':
                message = input("What would you like to write?\n")
                theReader.append(message)
            elif choice == '4':
                message = input("What would you like to write?\n")
                theReader.writeCSV(message)
            elif choice == '5':
                theReader.readCSV()
            elif choice == '6':
                message = input("What would you like to write?\n")
                theReader.appendCSV(message)
            elif choice == '7':
                quit()
            else:
                print("invalid selection")
            choice = input("What would you like to do?\n")
        # # if d is selected
        # print("Have a nice day!")

    if __name__ == "__main__":
        main()