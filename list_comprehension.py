simple = [4, 7, 16, 21, 42, 49]
"""res = []
for i in simple:
    res.append(i * 2)
print(res)"""
duble = [i * 2 for i in simple if i % 2 == 0]
print(duble)

a = [i for i in range(10)]
print(a)
#nested loop
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(coordinates)

#Flattening a list of lists
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [val for row in mat for val in row]
print(res)