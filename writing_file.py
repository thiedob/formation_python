# Write mode: Creates a new file or truncates an existing file
"""
with open('file.txt','w')as f:
    f.write("New Text File created using write Python method")

f =  open('file.txt','r')
print(f.read())

# Append mode: Creates a new file or appends to an existing file

f = open('file.txt', 'a')
f.write("file edited using append mode")

f = open('file.txt','r')
print(f.read())

# Exclusive creation mode: Creates a new file, raises error if file exists
try:
    with open('file.txt','x')as f:
        f.write("file created with x mode exclusive creation mode")
except FileExistsError:
    print("File already Exists")
"""
#Writing to an Existing File

with open('file1.txt','w') as f:
    f.write("Written to the file.")

f = open("file1.txt","r")
print(f.read())

# Writing multiple lines to an existing file using writelines()
s = ["First line of text.\n", "Second line of text.\n", "Third line of text.\n"]

with open("file1.txt", "w") as f:
    f.writelines(s)
    
f = open("file1.txt","r")
print(f.read()) 