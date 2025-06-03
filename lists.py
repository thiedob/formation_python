""" Creating a Python list
a = [10, 20, "GfG", 40, True]

print(a)
print(a[0])  
print(a[1])  
print(a[2])  

#creating list with list constructor
a = list((1, 2, 3, 'apple', 4.5))  
print(a)

# Initialize an empty list
li = []
li.append(10)  
print("After append(10):", li) 
li.insert(0, 5)
print("After insert(0, 5):", li) 
li.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", li)
"""
adlist = ['apple', 'banana', 'cherry']

# Iterating over the list
for item in adlist:
    print(item)