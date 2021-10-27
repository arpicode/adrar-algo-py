# Exercice 3.5

# Ecrire un script qui demande l’âge d’un enfant à l’utilisateur. Ensuite, il l’informe de sa
# catégorie :
#   • "Poussin" de 6 à 7 ans
#   • "Pupille" de 8 à 9 ans
#   • "Minime" de 10 à 11 ans
#   • "Cadet" après 12 ans

# Peut-on concevoir plusieurs scripts équivalents menant à ce résultat ?

age = int(input("Entrez l'âge de l'enfant : "))

if age >= 6 and age <= 7:
    print('Poussin')
if age >= 8 and age <= 9:
    print('Pupille')
if age >= 10 and age <= 11:
    print('Minime')
if age >= 12:
    print('Cadet')

# Alternative 1

if age >= 6 and age <= 7:
    print('Poussin')
elif age >= 8 and age <= 9:
    print('Pupille')
elif age >= 10 and age <= 11:
    print('Minime')
elif age >= 12:
    print('Cadet')

# Alternative 2

if age >= 6 and age <= 7:
    print('Poussin')
else:
    if age >= 8 and age <= 9:
        print('Pupille')
    else:
        if age >= 10 and age <= 11:
            print('Minime')
        else:
            if age >= 12:
                print('Cadet')

# ... et d'autres
