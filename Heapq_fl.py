import heapq
"""li = [50, 20, 10, 53]
print(li)
heapq.heapify(li)
print("heap queue:",li)
heapq.heappush(li, 5)
print("heap queue:",li)
min = heapq.heappop(li)
print("min element of the heap queue:",min)
print("latest heap queue:",li)
# using heappushpop
newmin = heapq.heappushpop(li, 61)
print("New min element of the heap queue:",newmin)
print("latest heap queue:",li)

maxi = heapq.nlargest(2, li)
mini = heapq.nsmallest(2, li)
print(maxi)
print(mini)
"""

# Creating a heap
h1 = [10, 20, 15, 30, 40]
heapq.heapify(h1)

# Replacing the smallest element (10) with 5
min = heapq.heapreplace(h1, 5)

print(min)
print(h1)

# Merging Heaps
h2 = [2, 4, 6, 8]

# Merging the lists
h3 = list(heapq.merge(h1, h2))
print("Merged heap:", h3)