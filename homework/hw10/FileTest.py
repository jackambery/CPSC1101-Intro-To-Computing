

from FileReader import FileReader

class FileTest:
      
    def main():

        theReader = FileReader()
        
        while (True):
            
            print("Please type '1', '2', '3', '4', '5', '6', or '7' for whichever option you desire.")
            print("1) Write to the file.\n2) Read the file.\n3) Append to the file.\n4) Write to the CSV file.\n5) Read the CSV file.\n6) Append to the CSV file.\n7) Quit")

            choice = input("What would you like to do?\n")

            if choice == '1':
                message = input("What would you like to write to the file?\n")
                theReader.write(message)
            elif choice == '2':
                theReader.read()
            elif choice == '3':
                message = input("What would you like to append to the file?\n")
                theReader.append(message)
            # does not take user input right now
            elif choice == '4':
                print("ex. [ [key, value], [key, value], [key, value, value] ]")
                message = input("What would you like to write to the CSV?\n")
                theReader.writeCSV()
            elif choice == '5':
                theReader.readCSV()
            elif choice == '6':
                print("ex. [ [key, value], [key, value], [key, value, value] ]")
                message = input("What would you like to append to the CSV?\n")
                theReader.appendCSV(message)
            elif choice == '7':
                print("Have a nice day!")
                quit()
            else:
                print("invalid selection")

    if __name__ == "__main__":
        main()