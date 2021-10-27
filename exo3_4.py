# Exercice 3.4

# Ecrire un script qui demande deux nombres à l’utilisateur et l’informe ensuite si le produit est
# négatif ou positif (on inclut cette fois le traitement du cas où le produit peut-être nul).
# Attention toutefois, on ne doit pas calculer le produit !

number1 = float(input('Entrez le premier nombre : '))
number2 = float(input('Entrez le second nombre : '))

if (number1 <= 0 and number2 <= 0) or (number1 >= 0 and number2 >= 0):
    print('Le produit et positif.')
elif (number1 < 0 or number2 < 0):
    print('Le produit et négatif.')
