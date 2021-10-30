# Exercice 3.2

# Ecrire un script qui demande deux nombres à l’utilisateur et l’informe ensuite si leur produit est
# négatif ou positif (on laisse de côté le cas où le produit est nul).
# Attention toutefois : on ne doit pas calculer le produit des deux nombres.

def print_product_sign(num1: float, num2: float) -> None:
    if (num1 < 0 and num2 < 0) or (num1 > 0 and num2 > 0):
        print('Le produit est positif.')
    elif (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
        print('Le produit est négatif.')


if __name__ == '__main__':
    number1 = float(input('Entrez le premier nombre : '))
    number2 = float(input('Entrez le second nombre : '))

    print_product_sign(number1, number2)
