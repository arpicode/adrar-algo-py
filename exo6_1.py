# Exercice 6.1 :

# Ecrire un script qui déclare une liste vide puis la remplisse avec une liste de 7 zéros. Utiliser
# une boucle !

FILL_COUNT = 7
FILL_VALUE = 0

myList = []

for i in range(0, FILL_COUNT):
    myList.append(FILL_VALUE)

print(myList)
