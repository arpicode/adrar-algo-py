# Exercice 3.3

# Ecrire un script qui demande trois noms à l’utilisateur et l’informe ensuite s’ils sont rangés ou
# non dans l’ordre alphabétique.

def print_sorted(str1: str, str2: str, str3: str) -> None:
    if str1 <= str2 <= str3:
        print('Ordre alphabétique.')
    else:
        print('Ordre non-alphabétique.')


if __name__ == '__main__':
    name1 = input('Entrez le 1er nom : ')
    name2 = input('Entrez le 2ème nom : ')
    name3 = input('Entrez le 3ème nom : ')

    print_sorted(name1, name2, name3)
