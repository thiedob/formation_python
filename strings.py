#MULTIPLE LINES STRING
s = """I am Learning
Python String on GeeksforGeeks"""
print(s)

s = '''I'm a 
Geek'''
print(s)

#STRING SLICING
texte = "mon nouveau texte"
text1 = texte[2:8]
print(text1)

text2 = texte[0:5]
print(text2)   

text3 = texte[5:]
print(text3)   

# Reverse a string
text4 = texte[::-1]
print(text4)

#replace and strip strings
s = "   Gfg   "
print(s.strip())    

s = "Python is fun"
print(s.replace("fun", "awesome"))