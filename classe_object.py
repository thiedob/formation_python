#define a class
class Dog:
    #class attribute
    species = "Canine" #class attribute
    
    #using __init__function()
    def __init__(self, name, age):
        self.name = name #Instance attribute
        self.age = age #Instance attribute
    """
    def bark(self):
        print(f"{self.name} is barking")
    """
    #__str__ method
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
dog1 = Dog("linguere", 9)
dog2 = Dog("Charlie", 5)
#dog1.bark()
print(dog1)
print(dog2)

#Access class and instance variables
print(dog1.species)  # (Class variable)
print(dog1.name)     # (Instance variable)
print(dog2.name)     # (Instance variable)

# Modify instance variables
dog1.name = "Max"
print(dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)