# Exercice 3.2

# Ecrire un script qui demande deux nombres à l’utilisateur et l’informe ensuite si leur produit est
# négatif ou positif (on laisse de côté le cas où le produit est nul).
# Attention toutefois : on ne doit pas calculer le produit des deux nombres.

number1 = float(input('Entrez le premier nombre : '))
number2 = float(input('Entrez le second nombre : '))

if (number1 < 0 and number2 < 0) or (number1 > 0 and number2 > 0):
    print('Le produit est positif.')
elif (number1 < 0 and number2 > 0) or (number1 > 0 and number2 < 0):
    print('Le produit est négatif.')
