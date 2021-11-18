# Exercice 5.2 :

# Ecrire un script qui demande un nombre compris entre 10 et 20, jusqu’à ce que la réponse
# convienne. En cas de réponse supérieure à 20, on fera apparaître un message : « Plus petit ! », et
# inversement, « Plus grand ! » si le nombre est inférieur à 10.

MIN_NUMBER = 10
MAX_NUMBER = 20

number = float(
    input(f'Entrez un nombre compris entre {MIN_NUMBER} et {MAX_NUMBER} : '))

while number < MIN_NUMBER or number > MAX_NUMBER:
    if number < MIN_NUMBER:
        print('Plus grand !')

    if number > MAX_NUMBER:
        print('Plus petit !')

    number = float(
        input(f'Erreur : entrez un nombre compris entre {MIN_NUMBER} et {MAX_NUMBER} : '))

print(
    f'Le nombre {number} est bien compris entre {MIN_NUMBER} et {MAX_NUMBER}.')
