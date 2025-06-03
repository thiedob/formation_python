"""class Car:
    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model  

    def display(self):
        return self.brand, self.model

# Create an instance of Car
car1 = Car("Toyota", "Corolla")

# Call the display_info method
print(car1.display())  

class gfg:
    def __init__(self, topic):
        self._topic = topic  

    def topic(self):
        print("Topic:", self._topic)  


ins = gfg("Python")

ins.topic()
---------
def msg(name):
    return f"hello, {name}!"
f = msg
print(f("Anurag"))

def fun1(fun2, nom):
    return fun2(nom)
print(fun1(msg,"Bob"))

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Storing functions in a dictionary
d = {
    "add": add,
    "subtract": subtract
}

# Calling functions from the dictionary
print(d["add"](5, 3))       
print(d["subtract"](5, 3))

#LAMBDA EXPRESSION 
# Example: Check if a number is positive, negative, or zero
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(n(5))   
print(n(-3))  
print(n(0))
"""
# Example: Filter even numbers from a list
n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)
print(list(even))