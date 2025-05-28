"""
#basic input tags
name = input("Enter your name : ")
print("hello ", name, "Welcome!")

#printing single & multiple variables
s = "Bob"
print(s)
nom = "Alice"
age = 25
city = "New York"
print(nom, age, city)

#taking two inputs at a time
x, y = input("Enter two numerical values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
 
# taking three inputs at a time
x, y, z = input("Enter three numerical values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

#taking conditionnal input from user
age_input = input(" Enter your age ")
age  = int(age_input)
if age < 0:
	print("Enter a valid age. ")
elif age <18:
	print("You are a minor.")
elif age>=18 and age <65:
	print("You are an adult.")
else:
	print("You are a senior Citizen.")
"""

#output formating
amount = 150.75
print("Amount = ${:.3f}".format(amount))
#end Parameter with '@'
print("Python", end='@')
print("GeeksforGeeks")
#using f format
name = 'balde '
age = 33
print(f"my name is {name}, and i am {age} years")