# Lab 6
# CS 101: Lab #6
# Filename: lab6.py
# Date: 8 Nov 2021
#
# Name: John (Jack) Ambery
# A lab to practice ascii conversion

def codebreaker(code):
    answer = ""
    splitted = code.split()
    for num in splitted:
        answer += chr(int(num))
    return(answer)

def main():
    code = "113 117 105 116 105 110 032 116 105 109 101"
    message = codebreaker(code)
    print("The secret message is:", message)

if __name__ == "__main__":
    main()