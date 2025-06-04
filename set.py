#CREATING AND MANIPULATING SETS
"""
S = {1, 15.0, "Modou", 45}
print(S)

set1 = set()
print(set1)
print(type(set1))

set1 = set("GeeksForGeeks")
print(set1)

# Creating a Set with the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print(set1)

# Creating a Set with the use of a tuple
tup = ("Geeks", "for", "Geeks")
set1 = set(tup)
print(set1)
#print(set(tup))

# Creating a Set with the use of a dictionary
d = {"Geeks": 1, "for": 2, "Geeks": 3}
set1 = set(d)
#print(set1)
print(set(d))

#Add and Update Methods
# Creating a set
set1 = {1, 2, 3}
print(set1)
# Add one item
set1.add(4)
print(set1)
# Add multiple items
set1.update([5, 6])
print(set1)

#Remove elements from a set
set1 = {1, 2, 3, 4, 5}
set1.remove(3)
print(set1)  

# Attempting to remove an element that does not exist
try:
    set1.remove(10)
except KeyError as e:
    print("Error:", e)  

# Using discard() Method
set1.discard(4)
print(set1)  

# Attempting to discard an element that does not exist
set1.discard(10)  # No error raised
print(set1)
"""