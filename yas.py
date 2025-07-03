"""
Menu  all menu request #155# and #100# (entering menu #155# et #100#)
if wrong number reject 
"""
import sys
import os

def effacer():
    try:
        os.system('clear')
    except:
        pass

def quitter():
    effacer()
    try:
        sys.exit()
    except SystemExit as e:
        print("Vous avez atteint 3 tentatives merci de revenir ulterieurement")

def verifier_numero(numero):
    """Fonction pour verifier qu'un numero est correct """
    longeur = len(numero)
    test = True if longeur == 9 else False
    cpt = 0
    if test:
        if numero[0]+numero[1] != "76":
            print("un numero correct doit commencer par 76")
        else:
            rest_num = numero[2:]
            for i in range(len(rest_num)):
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
    """Fonction pour verifier qu'un numero est saisi 3* sinon on arrete le programme """
    cpt = 0
    test = 0
    while test == 0 and cpt <3:
        try:
            numero = input("Entrez le numero mobile souhaite: ")
            check = verifier_numero(numero)
            if check == True:
                test = 1
            else:
                test = 0
                cpt += 1 
        except :
            cpt += 1
    if cpt == 3 and test == 0:
        quitter()
        return False
    elif cpt <= 3 and test == 1:
        return numero
    

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
        except:
            print("Veuillez choisir un entier parmi les choix ci-dessous")
            print(chaine)
            test = 0
            cpt += 1
    if cpt == 3:
        quitter()
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
        quitter() 
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
                test = 1
                print("Internet")
                print("1:3000F = 24Go+300mn+100SMS")
                print("2:Pass Jour")
                print("3:Pass 7J")
                print("4:Pass 30J")
                print("5:Bougna Internet")
                print("6:Mixx by Yas")
                print("7:Configurer son mobile")
                print("8:Mbakuss")
                choice = valider_choix("12345678")
                match choice:
                    case 1:
                        print("Mes offres")
                        print("1. 2500F = 15Go 30j")
                        print("2. 2000F = 15Go+250mn-30j")
                        print("3. 3000F = 24Go+300mn+100SMS ")
                        print("4. 2500F = 6Go+160Mn_30J ")
                        choice1 = valider_choix("1234")
                        if choice1 == 1:
                            print("Vous allez activer le forfait 15Go a 2500F valide 30J")
                            print("1:Confirmer")
                            choice2 = valider_choix("1")
                            if choice2 == 1:
                                print("Votre demande est en cours de traitement.Un sms vous sera envoye")
                        elif choice1 == 2:
                            print("Vous allez activer le forfait Illimax 2000F: 15Go+250mn+100SMSts reseaux valable 30j")
                            print("1:Confirmer")
                            choice2 = valider_choix("1")
                            if choice2 == 1:
                                print("Votre demande est en cours de traitement.Un sms vous sera envoye")
                        elif choice1 == 3:
                            print("Vous allez acheter la promo ILLIMAX 3000F valable 30j: 300mn+24Go+100SMS")
                            print("1:Confirmer")
                            choice2 = valider_choix("1")
                            if choice2 == 1:
                                print("Votre demande est en cours de traitement.Un sms vous sera envoye")
                        elif choice1 == 4:
                            print("Vous allez activer le forfait Illimax 2500F avec -6Go d'internet 160mntous reseau -400mn vers Free A 2500 Valide 30J")
                            print("1:Confirmer")
                            choice2 = valider_choix("1")
                            if choice2 == 1:
                                print("Votre demande est en cours de traitement.Un sms vous sera envoye")
                    case _:
                        pass
            case "#155#":
                test = 1
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
                #test = 1
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
                        elif choice1 == 3:
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
                                        print("Votre requete est en cours de traitement")
                                    elif choice3 == 2:
                                        numero = check_iteration()
                                        if numero != False:
                                            print("Vous allez acheter un Tawfekh 500F valable 24h pour le ",numero)
                                            print("1.Confirmer")
                                            choice4 = valider_choix("1")
                                            if choice4 == 1:
                                                print("Votre demande est en cours de traitement.Un sms vous sera envoye")
                                        else:
                                            quitter()
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
                    quitter()

def affiche_match155():
    pass        

def compter():
    pass
    #cpt = 1

saisir_code()