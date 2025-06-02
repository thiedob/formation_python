""" FUNCTIONS IN PYTHON
# defining and calling functions
def func():
    print("Hello")
   
func()

def salut():
    print("hello peps")

salut()
----------------
#function substraction
def substract(x, y):
    return (x-y)
a = 12 
b = 8 
resultat = substract(a, b)
print("resultat =",resultat)

def fun(n):
    x = 2
    count = 0
    while count < n:
        for d in range(2, int(x ** 0.5) + 1):  
            if x % d == 0:
                break  
        else:
            print(x)  
            count += 1
        x += 1

#TEST
n = 10
fun(n)

#FUNCTION WITH VARIABLE ARGUMENTS
def fun(*args):
    for arg in args:
        print(arg)

# Calling the function with multiple arguments
fun(1, 2, 3, 4, 5)

def fun(**kwargs):
    for k, val in kwargs.items():
        print(f"{k}: {val}")

# Calling the function with keyword arguments
fun(name="Alice", age=30, city="New York")
"""
class Person:
    # Constructor to initialize the person's name and age
    def __init__(self, name, age):
        self.name = name  # Set the name attribute
        self.age = age    # Set the age attribute
    
    # Method to print a greeting message
    def greet(self):
        print(f"Name - {self.name} and Age - {self.age}.")

# Create an instance of the Person class
p1 = Person("Alice", 30)

# Call the greet method to display the greeting message
p1.greet()