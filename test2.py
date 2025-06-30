"""
Menu  all menu request #155# and #100# (entering menu #155# et #100#)
if wrong number reject 
"""
import sys

def valider_choix(chaine = "123456789"):
    #pass
    test1 = 0
    while test1 == 0:
        try:
            choix = int(input("Veuillez entrer votre choix "))
            trouve = False if str(choix) not in chaine else True
            if trouve:
                test1 = 1
                print("CHOIX CORRECT")
                print(choix)
            else:
                print("Vous devez saisir un chiffre entre 1 et 9")               
                test1 = 0    
        except:
            print("Veuillez saisir un nombre entier")
    return choix

def saisir_code():
    #pass
    test = 0
    cpt = 0
    while test == 0 and cpt <3:
        saisi = input("Veuillez entrez le code souhaite: ")

        match saisi:
            case "#100#":
                print("Vous avez choisi l'option #100#")
                test = 1
            case "#155#":
                #print("Vous avez choisi l'option #155#")
                print("Portail YAS")
                print("1:3000F = 24Go+300mn+100SMS")
                print("3:Illimax")
                print("7:Internet")
                print("2:Voix")
                print("4:Bougna")
                print("5:International")
                print("6:Infos Utiles")
                print("8:Changement Nom Reseau")
                print("9:NOUVEAU:MYCANAL")
                choice = valider_choix()
                test = 1
                match choice:
                    case 1:
                        pass
                        choice1 = valider_choix("12345")
                    case 2:
                        pass
                        choice1 = valider_choix("012")
                    case 3:
                        pass
                        choice1 = valider_choix("012")
                    case 4:
                        pass
                        choice1 = valider_choix("012")
                    case 5:
                        pass
                        choice1 = valider_choix("012")
                    case 6:
                        pass
                        choice1 = valider_choix("012")
                    case 7:
                        pass
                        choice1 = valider_choix("012")
                    case 8:
                        pass
                        choice1 = valider_choix("012")
                    case 9:
                        pass
                        choice1 = valider_choix("012")
                    case _:
                        print("Veuillez saisir un choix correct")
                print(" ")            
                #choice = valider_choix()
            case _:
                print("Le code a saisir doit etre #100# ou #155#")
                test = 0
                cpt +=1
                if cpt == 3:
                    try:
                        sys.exit()
                    except SystemExit as e:
                        print("Vous avez atteint 3 tentives merci de revenir une prochaine fois")
                        
def affiche_match155():
    pass        

saisir_code()