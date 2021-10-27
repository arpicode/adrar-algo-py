# Exercice 3.1

# Ecrire un script qui demande un nombre à l’utilisateur, et l’informe ensuite si ce nombre est
# positif ou négatif (on laisse de côté le cas où le nombre vaut zéro).

number = float(input('Entrez un nombre : '))

if number < 0:
    print('Le nombre est négatif.')
if number > 0:
    print('Le nombre est positif.')
