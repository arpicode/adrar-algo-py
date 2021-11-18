# Exercice 5.1 :

# Ecrire un script qui demande à l’utilisateur un nombre compris entre 1 et 3 jusqu’à ce que la
# réponse convienne.

MIN_NUMBER = 1
MAX_NUMBER = 3

number = float(
    input(f'Entrez un nombre compris entre {MIN_NUMBER} et {MAX_NUMBER} : '))

while number < MIN_NUMBER or number > MAX_NUMBER:
    number = float(input(
        f'Erreur : entrez un nombre compris entre {MIN_NUMBER} et {MAX_NUMBER} : '))

print(
    f'Le nombre {number} est bien compris entre {MIN_NUMBER} et {MAX_NUMBER}.')
