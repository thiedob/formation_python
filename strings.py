"""S = "gfc"
print(S)
S1 = S + S[0]
print(S1)
#print(type(S))
#print(type(S1))

#MULTIPLE LINES STRING
s = '''I am Learning
Python String on GeeksforGeeks'''
print(s)

s = '''I/'m a 
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

test = "geeksforGeeks"
print(test)
test1 = "G" +test[1:]
print("apres concatenation test = ",test)
del test1
print(test1)
"""
s = "hello Geeks"
s1 = "H" + s[1:]
print(s)
print(s1)
s2 = s1.replace("Geeks", "geeksforGeeks")
print(s2)
"""
#replace and strip strings
s = "   Gfg   "
print(s.strip())    

s = "Python is fun"
print(s.replace("fun", "awesome"))
"""