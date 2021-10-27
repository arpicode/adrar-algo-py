# Exercice 3.3

# Ecrire un script qui demande trois noms à l’utilisateur et l’informe ensuite s’ils sont rangés ou
# non dans l’ordre alphabétique.

name1 = input('Entrez le 1er nom : ')
name2 = input('Entrez le 2ème nom : ')
name3 = input('Entrez le 3ème nom : ')

if name1 <= name2 <= name3:
    print('Ordre alphabétique')
else:
    print('Ordre non-alphabétique')
