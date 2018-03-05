"""
Script for the Python Workshop - Part 11 : Write/Read data files
Charlotte HERICE - Dec 2017
Just un-comment the part you want to execute
"""

myFile = open("../Data/test.txt", "r")
print(myFile)
myFile.close()

#########################

# myFile = open("../Data/test.txt", "r")
# myText = myFile.read()
# print(myText)
# myFile.close()

# #########################

# myFile = open("../Data/test.txt", "r")
# firstLine = myFile.readline()
# first2letters = myFile.readline(2)
# print("First word of the file:", firstLine)
# print("First 2 letters:", first2letters)
# myFile.close()

# #########################

# myFile = open("../Data/test.txt", "r")
# allLines = myFile.readlines()
# print("All lines of the file:", allLines)
# myFile.close()

# #########################

# myWords = []
# myFile = open("../Data/test.txt", "a")
# myFile.write("\n")
# myFile.write("Fine, thanks")
# myFile.close()

# #########################

# myFile = open("../Data/test.txt", "r")
# allLines = myFile.readlines()
# for line in allLines:
# 	words = line.split()
# 	print(words)
# myFile.close()







