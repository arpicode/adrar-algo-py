# Exercice 3.5

# Ecrire un script qui demande l’âge d’un enfant à l’utilisateur. Ensuite, il l’informe de sa
# catégorie :
#   • "Poussin" de 6 à 7 ans
#   • "Pupille" de 8 à 9 ans
#   • "Minime" de 10 à 11 ans
#   • "Cadet" après 12 ans

# Peut-on concevoir plusieurs scripts équivalents menant à ce résultat ?

def print_age_group(age) -> None:
    if age > 11:
        print('Cadet')
    elif age > 9:
        print('Minime')
    elif age > 7:
        print('Pupille')
    elif age > 5:
        print('Poussin')


# Alternative 1
def print_age_group_alt1(age) -> None:
    if age >= 6 and age <= 7:
        print('Poussin')
    elif age >= 8 and age <= 9:
        print('Pupille')
    elif age >= 10 and age <= 11:
        print('Minime')
    elif age >= 12:
        print('Cadet')


# Alternative 2
def print_age_group_alt2(age) -> None:
    if age >= 6 and age <= 7:
        print('Poussin')
    if age >= 8 and age <= 9:
        print('Pupille')
    if age >= 10 and age <= 11:
        print('Minime')
    if age >= 12:
        print('Cadet')


# Alternative 3
def print_age_group_alt3(age) -> None:
    if age >= 6 and age <= 7:
        print('Poussin')
    else:
        if age >= 8 and age <= 9:
            print('Pupille')
        else:
            if age >= 10 and age <= 11:
                print('Minime')
            else:
                if age >= 10:
                    print('Cadet')


# ... et d'autres variations...


if __name__ == '__main__':
    age = int(input("Entrez l'âge de l'enfant : "))

    print_age_group(age)
    print_age_group_alt1(age)
    print_age_group_alt2(age)
    print_age_group_alt3(age)
