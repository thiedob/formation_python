"""def greet():
    msg = "Hello from inside the function!"
    print(msg)

greet()

def greet():
    msg = "Hello!"
    print("Inside function:", msg)

greet()
#print("Outside function:", msg)

msg = "Python is awesome!"

def display():
    print("Inside function:", msg)

display()
print("Outside function:", msg)
"""
def fun():
    global s
    s += ' GFG'   
    print(s)
    s = "Look for Geeksforgeeks Python Section"
    print(s)

s = "Python is great!"
fun()
print(s)