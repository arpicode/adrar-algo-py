# Exercice 5.6 :

# Ecrire un script qui demande un nombre de départ, et qui calcule la somme des entiers jusqu’à ce
# nombre. Par exemple, si l’on entre 5, le programme doit calculer :
# 1 + 2 + 3 + 4 + 5 = 15
# NB : on souhaite afficher uniquement le résultat, pas la décomposition du calcul.

number = int(input('Entrez un nombre : '))

print(f'Somme de 1 à {number} : {int(number * (number + 1) / 2)}')
