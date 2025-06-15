#Inheritance in python
"""
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name  # Initialize the name attribute

    def speak(self):
        pass  # Placeholder method to be overridden by child classes

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"  # Override the speak method

# Creating an instance of Dog
dog = Dog("Buddy")
print(dog.speak())

# A Python program to demonstrate inheritance
class Person(object):
    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id
    # To check if this person is an employee    
    def Display(self):
        print(self.name, self.id)
emp = Person("Satyam", 102)
emp.Display()

class Emp(Person):
  
  def Print(self):
    print("Emp class called")
    
Emp_details = Emp("Mayank", 103)

# calling parent class function
Emp_details.Display()

# Calling child class function
Emp_details.Print()
"""

# Parent Class: Person
class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def Display(self):
        print(self.name)
        print(self.idnumber)

# Child Class: Employee
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)  # Calls Person's __init__()
        self.salary = salary
        self.post = post
human1 = Employee("jean", 14, 150000, "trainer")
human1.Display()
