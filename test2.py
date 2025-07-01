"""
Menu  all menu request #155# and #100# (entering menu #155# et #100#)
if wrong number reject 
"""
import sys
import os


def valid_choix(chaine = ['1','2','3','4','5','6','7','8','9']):
    cpt = 0
    car = len(chaine)
    test = 0
    while test == 0 and cpt <3:
        try:
            choix = int(input("Veuillez entrer votre choix "))
            for i in  chaine:
                trouve = True if i == str(choix) else False
                if trouve :
                    test = 1
                    break
            if not trouve:
                test = 0
                cpt += 1
                print("Veuillez choisir un entier parmi les choix ci-dessous")
                print(chaine)
                #pass
        except:
            #pass
            print("Veuillez choisir un entier parmi les choix ci-dessous")
            print(chaine)
            test = 0
            cpt += 1
    if cpt == 3:
        os.system('clear')
        try:
            sys.exit()
        except SystemExit as e:
            print("Vous avez atteint ",cpt," tentatives merci de revenir une prochaine fois")   
    else:
        os.system('clear')
        return choix
    #pass

def valider_choix(chaine = "123456789"):
    cpt = 0
    debut = chaine[0]
    fin = chaine[-1]
    test = 0
    while test == 0 and cpt <3:
        try:
            choix = int(input("Veuillez entrer votre choix "))
            trouve = False if str(choix) not in chaine else True
            if trouve :
                test = 1
                #print("CHOIX CORRECT")
            else:
                test = 0
                cpt +=1
                if chaine == "1":
                    print("1 est le seul choix possible merci de Rectifier")
                else:    
                    print("Vous devez saisir un chiffre entre ",debut," et ",fin)     
                continue            
        except:
            print("Veuillez saisir un nombre entier")
            test = 0
            cpt += 1
    if cpt == 3:
        os.system('clear')
        try:
            #print(cpt)
            sys.exit()
        except SystemExit as e:
            print("Vous avez atteint ",cpt," tentatives merci de revenir une prochaine fois")   
    else:
        os.system('clear')
        return choix


def saisir_code():
    #pass
    test = 0
    cpt1 = 0
    while test == 0 and cpt1 <3:
        saisi = input("Veuillez entrez le code souhaite: ")

        match saisi:
            case "#100#":
                print("Vous avez choisi l'option #100#")
                test = 1
            case "#155#":
                #print("Vous avez choisi l'option #155#")
                print("Portail YAS")
                print("1:Bons plans")
                print("3:Illimax")
                print("7:Internet")
                print("2:Voix")
                print("4:Bougna")
                print("5:International")
                print("6:Infos Utiles")
                print("8:Changement Nom Reseau")
                print("9:NOUVEAU:MYCANAL")
                #os.system('clear')
                choice = valider_choix()
                test = 1
                match choice:
                    case 1:
                        #pass
                        print("Mes offres")
                        print("1. 1000F = 5Go+30j")
                        print("2. 2000F = 15Go+250mn-30j")
                        print("3. 3000F = 24Go+300mn+100SMS ")

                        choice1 = valider_choix("123")
                        if choice1 == 1:
                            print("Vous allez activer le forfait 5Go a 1000F valide 30J")
                            print("1:Confirmer")
                            choice2 = valider_choix("1")
                            if choice2 == 1:
                                print("Votre demande est en cours de traitement.Un sms vous sera envoye")
                        elif choice1 == 2:
                            print("Vous allez activer le forfait Illimax 2000F: 15Go+250mn+100SMSts reseaux valable 30J")
                            print("1:Confirmer")
                            choice2 = valider_choix("1")
                            if choice2 == 1:
                                print("Votre demande est en cours de traitement.Un sms vous sera envoye")
                        else:
                            print("Vous allez acheter la promo ILLIMAX 3000F valable 30j: 300mn+24Go+100SMS")
                            print("1:Confirmer")
                            choice2 = valider_choix("1")
                            if choice2 == 1:
                                print("Votre demande est en cours de traitement.Un sms vous sera envoye")
                    case 2:
                        #pass
                        print("Offres Voix")
                        print("1:Tawfekh")
                        print("2:Samawaye")
                        print("0:Accueil ")
                        choice1 = valider_choix("012")
                        match choice1:
                            case 1:
                                print("Tawfekh(Tous reseaux)")
                                print("5:200F: 50Min-24h")
                                print("1:500F: 130Min-24h")
                                print("2:1000F: 400 Min-7j")
                                print("3:2000F: 750 Min-30j")
                                print("4:5000F: 1650 Min-30j")
                                print("0: Accueil")
                                #pass
                                choice2 = valider_choix("012345")
                                if choice2 == 1:
                                    print("130min ts reseaux valable 24h a 500F")
                                    print("1:Confirmer")
                                    print("2:Acheter pour un autre")
                                    print("99.Precedent")
                                    print("0.Accueil") 
                                    choice3 = valid_choix(['1','2','99','0']) 
                                    if choice3 == 1:
                                        #pass 
                                        print("Votre requete est en cours de traitement")
                                elif choice2 == 2:
                                    pass
                            case 2:
                                pass
                            case _:
                                pass
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
                        #print("Veuillez saisir un choix correct")
                        """print(choice)
                        cpt1 +=1
                        #print("Le code a saisir doit etre #100# ou #155#")
                        test = 0
                        if cpt1 == 3:
                            try:
                                sys.exit()
                            except SystemExit as e:
                                print("Vous avez atteint 3 tentives merci de revenir une prochaine fois")
                        """
                print(" ")            
                #choice = valider_choix()
            case _:
                cpt1 +=1
                print("Le code a saisir doit etre #100# ou #155#")
                test = 0
                if cpt1 == 3:
                    try:
                        sys.exit()
                    except SystemExit as e:
                        print("Vous avez atteint 3 tentives merci de revenir une prochaine fois")

def affiche_match155():
    pass        

def compter():
    pass
    #cpt = 1

saisir_code()