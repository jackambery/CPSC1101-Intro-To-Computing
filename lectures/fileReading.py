'''
steps:
1. open the file with an open type
    open(filename, open type)
    w - write
    r - read
    a - append
    b - binary
2. do stuff to file
3. close file

- if filename doesn't exist, the file is created

---helpful commands---
with open("myFile.txt", "w") as outfile:
    outfile.write

myFile.read() - reads whole file
myFile.readLine()
myFile.readLines()


'''