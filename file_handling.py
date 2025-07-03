# Open the file and read its contents
#with open('geeks.txt', 'r') as file:

#reading a file in normal mode
"""
file = open('tuto.txt','r')   
content = file.read()
print(content)
file.close()

#reading a file in binary mode
file = open("tuto.txt", "rb")
contenue = file.read()
print(contenue)
file.close()

#writing to a file
file = open("tuto.txt", "w")
file.write("ceci est le nouveau texte ecrit depuis le language python")
file.close()


file = open("tuto.txt", "rb")
contenue = file.read()
print(contenue)
file.close()

open("tuto.txt","r")        #Read mode
open("tuto.txt","rb")       #Read binary mode
open("tuto.txt","r+")       #Read and write mode
open("tuto.txt","rb+")      #Read and write in binary mode
open("tuto.txt","w")        #write mode
open("tuto.txt","wb")       #write in binary mode
open("tuto.txt","w+")       #write and read mode
open("tuto.txt","wb+")
open("tuto.txt","a")
open("tuto.txt","ab")
open("tuto.txt","a+")
open("tuto.txt","ab+")
open("tuto.txt","x")
open("tuto.txt","xb")
open("tuto.txt","x+")
open("tuto.txt","xb+")
open("tuto.txt","xb")

file = open('tuto.txt','r')
contenue = file.read()
print(contenue)
file.close()

file = open('tuto.txt','w')  #Editing file with write mode
file.write('Ceci est un nouveau texte ajoute a partir du fichier python avec le write mode il efface l\'ancien contenue et le remplace par le nouveau')
file.close()

file = open('tuto.txt','r')
contenue = file.read()
print(contenue)
file.close()

file = open('tuto.txt','a')
file.write('\n this is the text added using the append mode')
file.close()

file = open('tuto.txt','r')
contenue = file.read()
print(contenue)
file.close()

with open('fichier1.txt', 'x') as file:
    file.write("Nouveau fichier creer avec l4usage de with")


with open('fichier1.txt','r') as file:
    texte = file.read()
    print(texte)  

#file handling with exceptions 
try:
    file = open('fichier1.txt','r')
    content = file.read()
    print(content)
finally:
    file.close()

file = open('fichier1.txt','a')
file.write("Elle est issue d\’une riche famille aristocratique, influente en politique. Son père, Zulfikar Ali Bhutto, fondateur du Parti du peuple pakistanais (PPP, socialiste), dirige le pays de 1971 à 1977 en tant que président de la République puis Premier ministre. Après le coup d'État ayant évincé son père, qui est ensuite exécuté par le régime militaire de Muhammad Zia-ul-Haq, Benazir Bhutto se hisse à la tête de l'opposition et revendique l'héritage de son père en prenant le contrôle du PPP.Benazir Bhutto devient la première femme élue démocratiquement à la tête d'un pays musulman à la suite des élections législatives de 1988, et engage un tournant libéral au sein du PPP. Elle est destituée par le président Ghulam Ishaq Khan en 1990 et perd les élections de la même année. Elle retrouve la tête du gouvernement après le scrutin législatif de 1993. Accusée de corruption et violences claniques, elle termine son second mandat en 1996 avec un ordre de destitution du président Farooq Leghari. Afin d'échapper aux poursuites judiciaires, elle s'exile à Dubaï puis à Londres.Ayant obtenu du président Pervez Musharraf une amnistie, elle rentre au Pakistan pour participer aux élections législatives de 2008. Alors qu’elle s’associe avec Nawaz Sharif contre Musharraf, elle est tuée lors d'un attentat-suicide après un meeting à Rawalpindi. Les élections sont finalement remportées par son parti et son mari, Asif Ali Zardari, devient ensuite président de la République. Elle est la mère de l'homme politique ")
file.close()
"""

file = open('fichier1.txt','r')
text = file.read()
print(text)
file.close()