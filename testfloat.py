"""
li = []

for i in range(1,6):
    #print(i)
    
    if i == 1:
        user = float(input(f"entrer le {i}er nombre decimal: "))
    else:
        user = float(input(f"entrer le {i}ème nombre decimal: "))
    li.append(user)
print(li)
-------------------------------------------
Name1, Name2, Name3 = input("Entrer 3 strings").split()
print("Name1:",Name1)
print("Name2:",Name2)
print("Name3:",Name3)

Using format with print()
amount = 150.750214
print("Amount: ${:.3f}".format(amount))

#Using Sep and end parameter
# end Parameter with '@'
print("Python", end='@')
print("GeeksforGeeks")
print("thiedo", end="**")
print("BALDE")
print("thiedo", "mansour", "ben", "loulou", sep="@")

# Taking input from the user
num = int(input("Enter a value: "))
add = num + 5

# Output
print("The sum is %d" %add)

print("affichage en mode float %f" %add)
print("affichage en mode float %x" %add)
print("affichage en mode float %o" %add)

import keyword  
print("the list of keyword is below")
print(keyword.kwlist)   
"""
"""
# 'for' loop example
for num in range(3):
    if num == 2:
        #print("on est arive a 2 on n'affiche pas l'iteration")
        continue  # Skip number 2
    print(num)
# Output: 0 1

# 'while' loop example
count = 0
while count < 4:
    count += 1
    if count == 3:
        print("on est arive a 3 on n'affiche pas l'iteration et break nous fait quitter la boucle")
        break  # Exit the loop when count reaches 4
    print(count)
# Output: 1 2

test1 = 0
    while test1 == 0:
        choix = int(input("Veuillez entrer un chiffre compris entre 1 et 9"))
        str(choix) not in test
"""