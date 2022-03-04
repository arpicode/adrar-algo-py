# Exercice 8_csv :

# Créer un programme qui permette de gérer une liste de course. Il doit permettre de :
#
# 1) Ajouter un élément à la liste de courses
# 2) Retirer un élément de la liste de courses
# 3) Afficher la liste de courses
# 4) Sauvegarder la liste dans un fichier

import csv


COLOR_LIGHT_GREEN = '\033[92m'
COLOR_LIGHT_MAGENTA = '\033[95m'
COLOR_LIGHT_CYAN = '\033[96m'
COLOR_END = '\033[0m'
BOLD = '\033[1m'
MSG_ERROR = '\033[30m\033[41m ERROR \033[0m'
MSG_WARNING = '\033[30m\033[43m WARNING \033[0m'
CHECK = '\033[32m✔\033[0m'
CROSS = '\033[31m✘\033[0m'

SAVEFILE_NAME = 'liste de courses.csv'


def display_menu() -> None:
    print()
    print(f"{COLOR_LIGHT_CYAN}Choisir une d'action :{COLOR_END}")
    print()
    print(f'\t{BOLD}1{COLOR_END} → Ajouter un élément.')
    print(f'\t{BOLD}2{COLOR_END} → Retirer un élément.')
    print(f'\t{BOLD}3{COLOR_END} → Afficher la liste de courses.')
    print(f'\t{BOLD}4{COLOR_END} → Terminer la saisie et sauvegarder.')
    print()


def ask_for_choice() -> int:
    try:
        return int(input(f"\t{COLOR_LIGHT_CYAN}Action N° ? {COLOR_END}"))
    except ValueError:
        return 0


def ask_for_product_to_add() -> None:
    shopping_list.append(input("Saisir l'élément à rajouter : "))
    print()
    print(
        f'{CHECK} {BOLD}{shopping_list[-1]}{COLOR_END} ajouté à la liste')


def ask_for_product_to_remove() -> None:
    if (len(shopping_list) == 0):
        print(f"{MSG_WARNING} La liste est vide ! Aucun élément à supprimer.")
    else:
        item = input("Saisir l'élément à supprimer : ")
        print()
        if shopping_list.count(item) != 0:
            shopping_list.remove(item)
            print(f'{CROSS} {item} supprimé de la liste')
        else:
            print(f"{MSG_WARNING} {item} n'est pas dans la liste !")


def display_shopping_list() -> None:
    print('Contenu de la liste :')
    print(f'{COLOR_LIGHT_GREEN}{shopping_list}{COLOR_END}')


def read_shopping_list(filename: str) -> list:
    liste = []
    try:
        with open(filename, newline='', encoding='UTF-8') as csvfile:
            filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in filereader:
                liste.append(row[0])
    except FileNotFoundError:
        print(f"{MSG_WARNING} '{filename}' n'éxiste pas et sera donc créée.")
    return liste


def save_shopping_list(filename: str) -> None:
    with open(filename, 'w', newline='', encoding='UTF-8') as csvfile:
        filewriter = csv.writer(
            csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for product in shopping_list:
            filewriter.writerow([product])


# Programme principal :

choice = 0
shopping_list = read_shopping_list(SAVEFILE_NAME)

display_shopping_list()

while choice != 4:
    display_menu()
    choice = ask_for_choice()
    print()

    if (choice == 1):
        # Ajouter un élément
        ask_for_product_to_add()

    elif (choice == 2):
        # Retirer un élément
        ask_for_product_to_remove()

    elif (choice == 3):
        # Afficher la liste
        display_shopping_list()

    elif (choice == 4):
        # Sauvegarder la liste
        save_shopping_list(SAVEFILE_NAME)
        # Quitter
        print(f'{COLOR_LIGHT_MAGENTA}Liste terminée, bon shopping !{COLOR_END}')
    else:
        print(f"{MSG_ERROR} Cette action n'existe pas !")
