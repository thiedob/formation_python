#DATA TYPE TESTING FILE
# a python variable can be assigns multiple data type
"""
x = 50
x = 60.5
print(x)
print(type(x))
x = "Hello World
x = ["geeks", "for", "geeks"]
x = ("geeks", "for", "geeks")

printing variables type
a = 5 
print("type a = ",type(a))
b = 5.
print("type b = ",type(b))
c = 2 + 4j
print("type c = ",type(c))

#String data type
s = 'Welcome to the Geeks World'
print(s)
print(type(s))
--Access String index
print(s[0])
print(s[1])
print(s[9])
print(s[-1])

#List data type
a = []
a = ['pauline', 24, "laure", 60, 'Mamy', 31]
print("Accessing element from the list")
print('a[0  ]=',a[0])
print(a[1])
print(a[2])
print(a[-1])
print(a[-2])
print(a)
print(type(a))

#tuple data type 
tup = () #E;pty tuple initiating but it need at least one comma to be a fonctional tuple
tup2 = ('Daniel', 'Louis', 'Beatrice', 'Cira')
print(tup2)
print(type(tup))
print(type(tup2))

#bool datas has value True/False
#tuple managment
s1 = set()
s1 = set("GeeksforGeeks")
print("Set with the use of String: ", s1)
print(s1)
s2 = set(["Geeks", "For", "Geeks"])
#print("Set with the use of List: ", s2)
for l in s2:
    print(l, end=" ")
# check if item exist in set    
print("Oumar" in s2)

#Dictionnaries
d = {}
d = {1:'thiedo', 2:'mamy', 3:'baba', 'Dany':'Marie'}
print(d['Dany'])
nom = d.get(1)
print(nom) """
#EXERCISE
fruits = ["apple", "banana", "orange"]
print(fruits)
fruits.append("grape")
print(fruits)
fruits.remove("orange")
print(fruits)
fruits.append("pinepale")
print(fruits)
fruits.remove("pinepale")
print(fruits)