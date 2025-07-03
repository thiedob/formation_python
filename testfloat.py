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

chaine = "771816114"
longeur = len(chaine)
print(longeur)
for i in range(len(chaine)):
    print(f"chaine{i} = ",chaine[i])
"""

import os
import sys

def verifier_numero(numero):
    longeur = len(numero)
    test = True if longeur == 9 else False
    cpt = 0
    if test:
        if numero[0]+numero[1] != "76":
            print("un numero correct doit commencer par 76")
        else:
            rest_num = numero[2:]
            for i in range(len(rest_num)):
                print(rest_num[i])
                if rest_num[i]  in "0123456789":
                    cpt = 1
                    continue
                else:
                    cpt == 0
                    break          
            if cpt == 0:
                print("un numero ne doit contenir que des chiffres de 0 a 9")
                return False
            else:
                return True
    else:
        print("un numero doit contenir 9 chiffres. Example 761234567")
        return False


def check_iteration():
    cpt = 0
    test = 0
    while test == 0 and cpt <3:
        try:
            numero = input("Entrez le numero mobile souhaite: ")
            check = verifier_numero(numero)
            print(check)
            if check == True:
                test = 1
            else:
                test = 0
                cpt += 1 
        except :
            cpt += 1
    if cpt == 3 and test == 0:
        try:
            #os.system('clear')
            sys.exit()
        except SystemExit as e:
            print("Vous avez atteint 3 tentatives merci de ")
    elif cpt <= 3 and test == 1:
        print("Votre numero est le :", numero)

check_iteration()