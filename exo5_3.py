# Exercice 5.3 :

# Ecrire un script qui demande un nombre de départ, et qui ensuite affiche les dix nombres suivants.
# Par exemple, si l'utilisateur entre le nombre 17, le programme affichera les nombres de 18 à 27.

PRINT_TIMES = 10

nombre = int(input('Entrez un nombre de départ : '))

for i in range(1, PRINT_TIMES + 1):
    print(nombre + i)
