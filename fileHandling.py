'''
Data is very important to proceed further and analysis is done on data for the growth of the company.
Earlier when there is no database the data is stored in files to access, modify and delete the data
from the file comes under file handling.

Types of files
There are two types of files in Python
1. Text File
2. Binary File
Text File stores the data in the form of characters whereas binary file store the data in the form of
bytes.

Modes of File
[When we open a file the file pointer will be at the beginning of file]

Mode        Description
----------------------------------------------------------
r      -    To read the data from file
w      -    To write the file if any data is present in the file it will be deleted
a      -    To append the data in file (Add to end of file)
r+     -    To read and write data in file (Read First)
w+     -    To write and read the data in file (Write First)
a+     -    To append and read the data from the file (Append First)

Function in FileHandling
1. open() - Used to open a file.
syntax - open("filename", "mode")
Ex - f = open("file.txt", "r")
2. read() - Used to read file in form of string
syntax - fileOpener.read()
Ex - x = f.read()
3. close() - Used to close file
syntax - fileOpener.close()
Ex = f.close()
'''
# f = open("file.txt", "r")
# x = f.read()
# print(x)
# f.close()

# f = open("file.txt", "w")
# f.write("Jai Shree Ram")
# f.close()

# f = open("file.txt", "a")
# f.write(" Jai Shree Hanuman")
# f.close()

# f = open("file.txt", "r+")
# x = f.read() 
# print(x)
# f.write("Hello World")

# f.close()

# f = open("file.txt", "w+")
# f.write("My name is Nitish")
# f.seek(0)
# x = f.read()
# print(x)

# f.close()


# f = open("file.txt", "a+")
# f.write("My name is Nitish")
# f.seek(0)
# t = f.tell()
# print(t)
# x = f.read()
# print(x)
# f.close()


# f = open("file.txt", "a+")
# f.write("My name is Nitish")
# t = f.tell()
# print(t)
# x = f.read()
# print(x)


# f = open("file.txt", "r")
# x = f.read(17)
# print(x)
# f.close()


# f = open("file.txt", "r")
# x = f.readline()
# print(x)
# f.close()

# f = open("file.txt", "r")
# x = f.readlines()
# for i in x:
#     print(i)
# f.close()