# Exercice 3.1

# Ecrire un script qui demande un nombre à l’utilisateur, et l’informe ensuite si ce nombre est
# positif ou négatif (on laisse de côté le cas où le nombre vaut zéro).

def print_sign(n: float) -> None:
    if n < 0:
        print('Le nombre est négatif.')
    if n > 0:
        print('Le nombre est positif.')


if __name__ == '__main__':
    number = float(input('Entrez un nombre : '))

    print_sign(number)
