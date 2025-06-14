from collections import Counter
"""
val = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
#creating a counter
ctr = Counter(val)

print(ctr)

# Creating a Counter from a list
ctr1 = Counter([1, 2, 2, 3, 3, 3])
# Creating a Counter from a dictionary
ctr2 = Counter({1: 2, 2: 3, 3: 1})
# Creating a Counter from a string
ctr3 = Counter("hello")

print(ctr1)
print(ctr2)
print(ctr3)

#accessing elements of the count
print(ctr1[1])
print(ctr1[2])
print(ctr1[3])
print(ctr1[4]) #element not present in the counter

#Updating counters
ctr = Counter([1, 2, 2])
print(ctr)
ctr.update([2, 3, 3, 3, 1, 4, 4])
print(ctr)
print(type(ctr))

ctr = Counter([1, 2, 2, 3, 3, 3])
items = list(ctr.elements())

print(items) 
print(type(items))

ctr = Counter([1, 2, 2, 3, 3, 3])
print(ctr)

common = ctr.most_common(2) 
print(common)

ctr.subtract([2, 3, 3])
print(ctr)
"""
ctr1 = Counter([1, 2, 2, 3])
ctr2 = Counter([2, 3, 3, 4])

# Addition
print(ctr1 + ctr2)  
# Subtraction
print(ctr1 - ctr2)  

# Intersection
print(ctr1 & ctr2)  
# Union
print(ctr1 | ctr2)