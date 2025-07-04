"""
#Reading a file with open function
file = open('fichier1.txt','r')     #Opening a file
contenue = file.read()              #reading the content of the file and assign it to the varible contenue
print(contenue)                     #printing the content of the file
file.close()                        #closing the file

#Reading the file using with statement
with open('fichier1.txt','r') as file:
    content = file.read()
    print(content)


#Reading a file line by line with for loop
file = open('fichier1.txt','r')
for line in file:
    print(line.strip())

file.close()


# Open the file in read mode
file = open("fichier1.txt", "r")

# Read the first line
line = file.readline()

while line:
    print(line.strip())
    line = file.readline()  # Read the next line

# Close the file
file.close()


#Reading a file line by line with readline() method
file = open('fichier1.txt','r')
line = file.readline()

while line:
    print(line.strip())
    line = file.readline

file.close()

file = open('fichier1.txt','rb')
content = file.read()
print(content)
file.close()

#Reading Specific Parts of a File
file = open('fichier1.txt','r')
content = file.read(300)
print(content)
file.close()

#Reading CSV Files in Python
import csv

with open('fichier.csv', newline='')as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvfile:
        print(row)
This code reads a CSV file line by line, parsing it into a list of values for each row.
"""

#Reading json Files in Python
import json
with open('fichier.json','r')as jsonfile:
    data = json.load(jsonfile)
    print(data)
#This code reads a CSV file line by line, parsing it into a list of values for each row.